import collections
from itertools import groupby
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.forms import all_valid
from django.shortcuts import render, redirect
from django.views import generic
import traceback
from partners.forms import RegisterForm, CitiesTableForm, CityFormSet
from partners.models import HomePageBaseConfig, BaseMenu, RegisterFair, EventVideo, CitiesTables, Images, SliderVideo
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import * 
from sendgrid.helpers.mail import Mail,Email,Content
from azeri import settings

# Create your views here.


class BaseIndexView(generic.TemplateView):
    template_name = "partners/home/index.html"

    def get_context_data(self, **kwargs):
        # print(datetime.now().strftime("%H:%M"))
        logo_url = self.request.GET.get('url')
        context = {}
        context['logo_url'] = logo_url
        context['object'] = HomePageBaseConfig.objects.filter(page_url='/').last()
        context['sing_up_link'] = BaseMenu.objects.filter(status=True).last().url
        return context


class AboutPageView(generic.TemplateView):
    template_name = "partners/about.html"

    def get_context_data(self, **kwargs):
        # print(datetime.now().strftime("%H:%M"))
        logo_url = self.request.GET.get('url')
        context = {}
        context['logo_url'] = logo_url
        context['object'] = HomePageBaseConfig.objects.filter(page_url='/about/').last()
        return context


class ContactPageView(generic.TemplateView):
    template_name = "partners/contact.html"

    def get_context_data(self, **kwargs):
        # print(datetime.now().strftime("%H:%M"))
        logo_url = self.request.GET.get('url')
        context = {}
        context['logo_url'] = logo_url
        context['object'] = HomePageBaseConfig.objects.filter(page_url='/contact/').last()
        return context


class OtherPageView(generic.View):
    template_name = "partners/fair.html"
    form_class = RegisterForm()
    model = RegisterFair

    def get(self, request, *args, **kwargs):
        base_url = self.make_url(kwargs.get('slug'))
        context = {}
        today_str = date.today().strftime("%-d %B %Y")  # Format: 9 December 2019
        context['today'] = today_str

        base_obj = HomePageBaseConfig.objects.filter(page_url__icontains=base_url).filter().last()
        # url_due_to_slug =
        last_fair_base_menu_item = BaseMenu.objects.filter(status=True).last()
        if base_url == last_fair_base_menu_item.url:
            context['form'] = RegisterForm()
            context['form_table'] = CityFormSet(prefix='table')
            obj_base = BaseMenu.objects.get(url=base_url)
            context['base_menu_object'] = obj_base.id
            context['events'] = EventVideo.objects.filter(show_register=obj_base)
            context['images'] = Images.objects.all()[:6]
            context['videos'] = SliderVideo.objects.all()[:3]

            # user count from 2019-03-01
            first_date = datetime(2019, 3, 1)
            context['register_count'] = RegisterFair.objects.filter(created_at__gte=first_date).count()

        if base_obj:
            context['object'] = base_obj
        else:
            context['page_not_found'] = True
        return render(request, self.template_name, context)
    
    


    def make_url(self, slug):
        return "/{}/".format(slug)
    

    

def generate_invoice_number(invoice_number):
    b = datetime.now().strftime("%d/%m/%Y")
    if not '-' in invoice_number:
        invoice_number = '81021122-001'
    number, random = invoice_number.split("-")
    if number == b.replace("/", "")[::-1]:
        a = int(random)
        a += 1
        if len(str(a)) == 1:
            random = "00" + str(a)
        elif len(str(a)) == 2:
            random = "0" + str(a)
        else:
            random = str(a)
        return number + "-" + random
    else:
        return b.replace("/", "")[::-1] + "-" + "001"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    table_form_class = CityFormSet
    success_url = 'succesful.html'

    def get(self, request, *args, **kwargs):
        return redirect(self.success_url)

    def form_valid(self, form):
        
        register = RegisterFair.objects.last()
        if self.request.is_ajax():
            contact = form.save()
            if register:
                if register.invoice_number:
                    invoice_number = register.invoice_number
                else:
                    invoice_number = "81021122-001"
            else:
                invoice_number = "81021122-001"
            contact.invoice_number = generate_invoice_number(invoice_number)
            contact.reference_url = self.request.POST.get("reference_url")
            contact.reg_loc = BaseMenu.objects.get(id=self.request.POST.get("reg_loc"))
            contact.save()
            table_formset = self.table_form_class(self.request.POST, prefix='table')
            print("self.request.POST:::: ", self.request.POST)
            
            try:
                sg = SendGridAPIClient(apikey = settings.SENDGRID_API_KEY)
                from_email = Email('Azeristudent.az <info@azeristudent.az>') 
                to_email = Email(self.request.POST.get("email"))
                subject ='Autumn Fair 2021'
                content = Content("text/plain",'Hi,we are so happy for you registered ou fair.We well touch in you with a day')
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.body)
            
          
            # subject = 'Welcome to AzeriStundnt'
            # message = 'Thanks for registering our fair'
            # recipient = self.request.POST.get("email")
            # try:
            #     send_mail(subject, message, 'apikey', [recipient], fail_silently = False)
            #     print('succes')
            # except :
            #     print('error')

            
            if all_valid(table_formset):
                for table in table_formset:
                    obj = table.save(commit=False)
                    obj.fk = contact
                    try:
                        obj.save()
                    except:
                        print(traceback.format_exc())
                return JsonResponse({
                    "save": True
                })
            else:
                return JsonResponse({
                    "save": False
                })
        

    def form_invalid(self, form):
        return JsonResponse({
            "save": False,
            "message": form.errors
        })



class DataAnalysis(LoginRequiredMixin, generic.TemplateView):
    template_name = 'analysis/report.html'

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['users_counts'] = RegisterFair.objects.count()
        ctx['data_spring'] = CitiesTables.objects.filter(fk__reg_loc__id=3, cities_id__isnull=False).values(
            'cities').annotate(sum_order=Sum("table_count"))
        ctx['data_spring_count'] = CitiesTables.objects.filter(fk__reg_loc__id=3, cities_id__isnull=False).aggregate(
            sum_order=Sum("table_count"))
        ctx['data_fall'] = CitiesTables.objects.filter(fk__reg_loc__id=5, cities_id__isnull=False).values(
            'cities').annotate(sum_order=Sum("table_count"))
        ctx['data_fall_count'] = CitiesTables.objects.filter(fk__reg_loc__id=5, cities_id__isnull=False).aggregate(
            sum_order=Sum("table_count"))
        return ctx
