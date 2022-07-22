from itertools import chain
from operator import attrgetter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.db.models import Max
from django.views import generic
from .models import uniLogoSlider,currencies
from partners.models import Universities
from student.forms import ContactUsForm, MainPageSearchForm, \
    EducationContactForm
from student.models import BaseSlider, Country, ContactUs, AboutUs, Service, News,Blog,Videos, Review, EducationCategory, Education, \
    Event, UnivercityProgram, HigherSpecial, Language, City, SchoolType, SecondaryProgram, LanguageProgram, \
    AccommondationEducation, EducationContact, WebsiteSetings, Exhibitions, ReservationDate, Insurance, ConnectApply, \
    Partners,FaqQuestion,FaqQuestionType

# Create your views here.
from student.options.tools import AGE_RESTRICTION, SEASON


class BaseIndexView(generic.TemplateView):
    """
        Home index View
        Base Azeristudent Homepage view
    """
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)
        context["sliders"] = BaseSlider.objects.filter(status=True)
        context["about"] = AboutUs.objects.all().last()
        context["services"] = Service.objects.all()
        context['unilogos'] = uniLogoSlider.objects.all()
        context["search_form"] = MainPageSearchForm(initial={
            'education_type': 1,
            'country': 2,

        })
        news_list = list(News.objects.all()[:6])
        event_list = list(Event.objects.all()[:6])
        result_list = sorted(
            chain(news_list, event_list),
            key=attrgetter('created_at'))[::-1]
        context["news_list"] = result_list
        context["review_list"] = Review.objects.all()[:3]
        return context


class CountryDetailView(generic.DetailView):
    """
        Base Country
        Detail view
    """
    model = Country
    template_name = "countries/detail.html"


# Modal Views contact us
class CountactUsFormView(generic.CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('successful')

    def get(self, request, *args, **kwargs):
        return redirect(self.success_url)

    def form_valid(self, form):
        if self.request.is_ajax():
            contact = form.save(commit=False)
            if self.request.POST.get('prefix', False):
                contact.phone = self.add_brackets(self.request.POST.get('prefix')) + contact.phone
            if self.request.POST.get('event_id', False):
                contact.event_id = self.make_int(self.request.POST.get('event_id'))
            contact.reference_url = self.request.POST.get("reference_url")
            contact.save()
            return JsonResponse({
                "save": True
            })

    def form_invalid(self, form):
        return JsonResponse({
            "save": False,
            "message": form.errors
        })

    def add_brackets(self, text):
        return "({}) ".format(text)

    def make_int(self, text):
        if text.isdigit():
            return int(text)
        else:
            return None


class AboutPageView(generic.TemplateView):
    template_name = "about_us/detail.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["object"] = AboutUs.objects.all().last()
        return context


class ServicesListView(generic.ListView):
    model = Service
    template_name = "services/list.html"


class ServicesDetailView(generic.DetailView):
    model = Service
    template_name = "services/detail.html"


class NewsListView(generic.ListView):
    model = News
    template_name = "news/list.html"
    paginate_by = 5
    


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "news/detail.html"


class BlogListView(generic.ListView):
    model = Blog
    template_name = "blog/list.html"
    paginate_by = 5
    


class VideoDetailView(generic.DetailView):
    model = Videos
    template_name = "videos/detail.html"


class VideoListView(generic.ListView):
    model = Videos
    template_name = "videos/list.html"
    paginate_by = 5
    

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/detail.html"

class ReviewListView(generic.ListView):
    model = Review
    template_name = "review/list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super(ReviewListView, self).get_queryset()
        if self.request.GET.get('status', False):
            if self.request.GET.get('status') == 'parent':
                return qs.filter(review_type=1)
            elif self.request.GET.get('status') == 'student':
                return qs.filter(review_type=0)
            else:
                return qs
        else:
            return qs


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = "review/detail.html"


class EducationCategoryListView(generic.DetailView):
    model = EducationCategory
    template_name = "education/detail.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(EducationCategoryListView, self).get_context_data(**kwargs)
        edu = self.object
        if edu.id == 3:
            context['lang_prog'] = True
            context['language'] = Language.objects.all()
            context['age_restriction'] = AGE_RESTRICTION
            context['season'] = SEASON
            context['lang_programs'] = LanguageProgram.objects.all()
            context['accomondation'] = AccommondationEducation.objects.all()
            context["education_list"] = self.get_programs()
        elif edu.id == 2:
            context['secon_edu'] = True
            context['secondary_program'] = SecondaryProgram.objects.all()
            context['language'] = Language.objects.all()
            context['scool_type'] = SchoolType.objects.all()
            context["education_list"] = self.get_programs()
        else:
            context['higher_edu'] = True
            context['univercity_program'] = UnivercityProgram.objects.all()
            context['special'] = HigherSpecial.objects.all()
            context['language'] = Language.objects.all()
            context['city_list'] = City.objects.all()
            context['scool_type'] = SchoolType.objects.all()
            context['currencies'] = currencies.objects.all()
            context["education_list"] = self.get_programs()
            
        return context

    def get_programs(self):
        education_list = Education.objects.filter(education_type=self.object)
        education_list = self.get_base_queryset(education_list)    
        paginator = Paginator(education_list, self.paginate_by)  # Show 3 per page
        page = self.request.GET.get('page')
        try:
            educations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            educations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            educations = paginator.page(paginator.num_pages)
        index = educations.number - 1  # edited to something easier without index
        # This value is maximum index of your pages, so the last page - 1
        max_index = len(paginator.page_range)
        # You want a range of 7, so lets calculate where to slice the list
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index - 5 else max_index
        context = {}
        context['paginator'] = paginator
        context['page_range'] = list(paginator.page_range)[start_index:end_index]
        context['is_paginated'] = True if education_list.count() > self.paginate_by else False
        context['data'] = educations
        context['count'] = education_list.count()
        context['education'] = self.object
       
        return context

    def get_base_queryset(self, object_list):
        if object_list.last():
            # have
            edu = self.object
            if edu.id == 3:
                result = {}
                country = self.request.GET.get('country', False)
                univercity_program = self.request.GET.get('univercity_program', False)
                specials = self.request.GET.get('specials', False)
                language = self.request.GET.get('language', False)
                city = self.request.GET.get('city', False)
                school_type = self.request.GET.get('school_type', False)
                age = self.request.GET.get('age', False)
                age_restriction = self.request.GET.get('age_restriction', False)
                
                if country and country != "":
                    result['country_id'] = country
                if univercity_program and univercity_program != "":
                    result['univercity_program'] = univercity_program
                if specials and specials != "":
                    result['specials'] = specials
                if language and language != "":
                    result['language'] = language
                if city and city != "":
                    result['city'] = city
                if school_type and school_type != "":
                    result['school_type'] = school_type
                if age and age != "":
                    result['age'] = age
                if age_restriction and age_restriction != "":
                    result['age_restriction'] = age_restriction
                '''if cost and cost != "":
                    result['uni_cost'] = cost'''
                return object_list.filter(**result)
            elif edu.id == 2:
                result = {}
                country = self.request.GET.get('country', False)
                univercity_program = self.request.GET.get('univercity_program', False)
                specials = self.request.GET.get('specials', False)
                language = self.request.GET.get('language', False)
                city = self.request.GET.get('city', False)
                school_type = self.request.GET.get('school_type', False)
                age = self.request.GET.get('age', False)
                

                if country and country != "":
                    result['country_id'] = country
                if univercity_program and univercity_program != "":
                    result['univercity_program'] = univercity_program
                if specials and specials != "":
                    result['specials'] = specials
                if language and language != "":
                    result['language'] = language
                if city and city != "":
                    result['city'] = city
                if school_type and school_type != "":
                    result['school_type'] = school_type
                if age and age != "":
                    result['age'] = age
                '''if cost and cost != "":
                    result['uni_cost'] = cost'''
                return object_list.filter(**result)
            else:
                result = {}
                country = self.request.GET.getlist('country', False)
                uniprog = self.request.GET.getlist('uniprog', False)
                specials = self.request.GET.get('specials', False)
                languages = self.request.GET.getlist('language', False)
                city = self.request.GET.get('city', False)
                school_type = self.request.GET.get('school_type', False)
                mincost    = self.request.GET.get('mincost',False)
                maxcost    = self.request.GET.get('maxcost',False)
                currency    = self.request.GET.get('currency',False)

                if country and len(country):
                    object_list = object_list.filter(country__id__in = country)
                if uniprog and len(uniprog):
                    object_list = object_list.filter(univercity_program__id__in =uniprog )
                
                if languages and len(languages):
                    object_list = object_list.filter(language__id__in =languages)
                """if city and city != "":
                    result['city'] = city
                if school_type and school_type != "":
                    result['school_type'] = school_type
                 """
               
                if mincost and maxcost:
                    
                    if  mincost == "":
                        mincost =  0
                    if  maxcost == "":
                        maximum = Education.objects.all().aggregate(Max('uni_cost'))
                        maxcost = maximum.get('uni_cost__max')   
                    if int(currency) != 0:
                        return object_list.filter(currency__id = currency).filter(uni_cost__range=(int(mincost),int(maxcost)) )
                    else:
                        return object_list
                else:
                    return object_list

        else:
            return object_list


class EventListView(generic.ListView):
    model = Event
    paginate_by = 3
    template_name = "events/list.html"
    ajax_template = "events/partials/event_list.html"

    def get_queryset(self):
        qs = super(EventListView, self).get_queryset()
        return qs.filter(publish_date__lte=timezone.now()).order_by("-event_date")

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['event_titles'] = self.model.objects.all().values('title', 'event_date')
        return context

    def get(self, *args, **kwargs):
        if self.request.is_ajax():
            bqs = self.get_queryset()
            date = self.request.GET.get('date')
            filter_date = timezone.datetime.strptime(date, "%Y-%m-%d %H:%M")
            context = {}
            context['object_list'] = bqs.filter(
                event_date__year=filter_date,
            )
            return render(self.request, self.ajax_template, context)
        else:
            return super(EventListView, self).get(*args, **kwargs)


class EventDetailView(generic.TemplateView):
    model = Event
    templates = "events/detail.html"

    def get(self, request, *args, **kwargs):
        data = self.model.objects.filter(slug=self.kwargs['slug']).first()
        if data is None:
            raise Http404()
        else:
            if data.exhibition:
                return redirect("exhibition", data.exhibition.slug)
            else:
                context = {
                    'object': data
                }
                return render(request, self.templates, context)


class EventArcihveView(generic.DayArchiveView):
    queryset = Event.objects.all()
    date_field = "event_date"
    month_format = "%m"
    allow_future = True
    allow_empty = True
    template_name = "events/list.html"

    def get_context_data(self, **kwargs):
        context = super(EventArcihveView, self).get_context_data(**kwargs)
        context['event_titles'] = Event.objects.all().values('title', 'event_date')
        return context


class UnivercityDetailView(generic.DetailView):
    model = Education
    template_name = "education/univercity/index.html"

    def get_queryset(self):
        qs = super(UnivercityDetailView, self).get_queryset()
        return qs.filter(education_type__slug=self.kwargs.get('education_slug'),
                         country__slug=self.kwargs.get('country_slug'))


class CounrtyEducationListView(generic.ListView):
    model = Education
    template_name = "education/detail.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CounrtyEducationListView, self).get_context_data(**kwargs)
        country = Country.objects.get(slug=self.kwargs.get('country_slug'))
        context['object'] = EducationCategory.objects.get(slug=self.kwargs.get('education_slug'))

        if context['object'].pk == 3:
            context['language'] = Language.objects.all()
            context['age_restriction'] = AGE_RESTRICTION
            context['season'] = SEASON
            context['lang_programs'] = LanguageProgram.objects.all()
            context['accomondation'] = AccommondationEducation.objects.all()
            context["education_list"] = self.get_programs()
        elif context['object'].pk == 2:
            context['secondary_program'] = SecondaryProgram.objects.all()
            context['language'] = Language.objects.all()
            context['scool_type'] = SchoolType.objects.all()
            context["education_list"] = self.get_programs()
        else:
            context['univercity_program'] = UnivercityProgram.objects.all()
            context['special'] = HigherSpecial.objects.all()
            context['language'] = Language.objects.all()
            context['city_list'] = City.objects.filter(country=country)
            context['scool_type'] = SchoolType.objects.all()
            context["education_list"] = self.get_programs()
        return context

    def get_paginate_by(self, queryset):
        pass

    def get_queryset(self):
        qs = super(CounrtyEducationListView, self).get_queryset()
        return qs.filter(education_type__slug=self.kwargs.get('education_slug'),
                         country__slug=self.kwargs.get('country_slug'))

    def get_programs(self):
        education_list = Education.objects.filter(
            education_type__slug=self.kwargs.get('education_slug'),
            country__slug=self.kwargs.get('country_slug')
        )
        paginator = Paginator(education_list, self.paginate_by)  # Show 3 per page
        page = self.request.GET.get('page')
        try:
            educations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            educations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            educations = paginator.page(paginator.num_pages)
        context = {}
        index = educations.number - 1  # edited to something easier without index
        # This value is maximum index of your pages, so the last page - 1
        max_index = len(paginator.page_range)
        # You want a range of 7, so lets calculate where to slice the list
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index - 5 else max_index
        context['is_paginated'] = True if education_list.count() > self.paginate_by else False
        context['paginator'] = paginator
        context['page_range'] = list(paginator.page_range)[start_index:end_index]
        context['data'] = educations
        context['count'] = education_list.count()
        context['country'] = Country.objects.filter(slug=self.kwargs.get('country_slug')).last()
        context['education'] = EducationCategory.objects.filter(slug=self.kwargs.get('education_slug')).last()
        return context


class ProgramsView(generic.TemplateView):
    template_name = "programs/index.html"


class ApplyView(generic.TemplateView):
    template_name = "special_events/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        last_apply = ConnectApply.objects.last()
        dt = last_apply.start_date - timezone.now()
        days = dt.days
        hours, remainder = divmod(dt.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        seconds += dt.microseconds / 1e6
        context['hours'] = round(hours)
        context['minutes'] = round(minutes)
        context['seconds'] = round(seconds)
        context['days'] = days
        # context['educations'] = Education.objects.filter(education_type__pk=1)[:40]
        context['partner'] = Partners.objects.all()[:8]
        context['educations'] = Universities.objects.all()
        return context


class EducationAjaxView(generic.View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            val = request.GET.get('value')
            data = self.get_country(val)
            print(data)
            return JsonResponse({
                "message": val
            })
        else:
            return JsonResponse({
                "message": "authorization required"
            })

    def get_country(self, val):
        arr = []
        for country in Country.objects.all():
            obj = Education.objects.filter(
                country=country,
                education_type__id=val
            )
            if obj.last():
                arr.append(country)
        return arr


class SearchFormView(generic.TemplateView):
    template_name = "home/partials/search.html"

    def get(self, request, *args, **kwargs):
        education = Education.objects.all()
        education_type = []
        country = []
        language = []
        for edu in education:
            if not edu.education_type in education_type:
                education_type.append(edu.education_type)
            if not edu.country in country:
                country.append(edu.country)

            for lang in edu.language.all():
                if not lang in language:
                    language.append(lang)
        context = {}
        context['education_type'] = education_type
        context['country'] = country
        context['language'] = language
        return render(request, self.template_name, context)

#search form 
class EducationSearchForm(generic.TemplateView):
    template_name = "education/partials/search.html"

    def get(self, request, *args, **kwargs):
        education_type_id = request.GET.get('type')
        education_type = EducationCategory.objects.get(id=education_type_id)
        context = {}
        education_list = Education.objects.filter(education_type=education_type)
        if request.GET.get('country'):
            context['country_name'] = Country.objects.filter(pk=request.GET.get('country')).last()
        if education_type_id == "1":
            # Higer education Search form
            context['country_list'] = Country.objects.all()
            context['univercity_program'] = UnivercityProgram.objects.all()
            context['special'] = HigherSpecial.objects.all()
            context['language'] = Language.objects.all()
            context['city_list'] = City.objects.all()
            context['scool_type'] = SchoolType.objects.all()
            context['education_type'] = 1
            return render(request, self.template_name, context)
        elif education_type_id == "2":
            # Secondary education Search form
            context['country_list'] = Country.objects.all()
            context['secondary_program'] = SecondaryProgram.objects.all()
            context['language'] = Language.objects.all()
            context['scool_type'] = SchoolType.objects.all()
            context['education_type'] = 2
            return render(request, self.template_name, context)
        else:
            # Language education search form
            context['country_list'] = Country.objects.all()
            context['language'] = Language.objects.all()
            context['age_restriction'] = AGE_RESTRICTION
            context['season'] = SEASON
            context['lang_programs'] = LanguageProgram.objects.all()
            context['accomondation'] = AccommondationEducation.objects.all()
            context['education_type'] = 3
            return render(request, self.template_name, context)
        # return JsonResponse({
        #     "status": "jn"
        # })


class EducationContactView(generic.CreateView):
    model = EducationContact
    form_class = EducationContactForm
    success_url = reverse_lazy('successful')

    def form_valid(self, form):
        obj = form.save(commit=False)
        edu_pk = self.request.POST.get('education')
        edu = Education.objects.get(pk=edu_pk)
        obj.univercity = edu
        obj.save()
        return JsonResponse({
            "save": True
        })


class GetContyCityView(generic.TemplateView):
    template_name = "partials/search_options.html"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            context = {}
            country = Country.objects.filter(pk=request.GET.get('id')).last()
            if country:
                context['options'] = City.objects.filter(country=country)
                return render(request, self.template_name, context)
            else:
                return JsonResponse({
                    "status": False
                })


# class TestingView(generic.TemplateView):
#     template_name = "testing.html"


class SuccessfulView(generic.TemplateView):
    template_name = "successful.html"

    def get_context_data(self, **kwargs):
        ctx = {'image': WebsiteSetings.objects.last()}
        return ctx


class ExhibitionDetails(generic.DetailView):
    template_name = "events/exhibitions.html"
    model = Exhibitions

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        # cxt['table_collection'] = ExhibitionContentType.objects.filter
        return cxt


class ReserveDateView(generic.TemplateView):
    template_name = "reserve/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now().date()
        current_time = datetime.now().time().strftime("%H")
        context['reserve_count'] = date_range(current_date, current_time)
        context['current_date'] = current_date

        # for education reserve options
        context['educations'] = Education.objects.filter(education_type__in={1, 2}).distinct()
        country = Education.objects.filter(education_type__in={1, 2}).values_list('country', flat=True)
        context['countries'] = Country.objects.filter(id__in=set(country))
        return context

class ReserveCountryUniAjaxView(generic.TemplateView):
    template_name = 'reserve/get_country_unis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # country_id = self.kwargs['country_id']
        if 'edu-cat' in self.request.GET and 'country' not in self.request.GET:
            edu_cat_id = self.request.GET['edu-cat']
            country = Education.objects.filter(education_type__pk=edu_cat_id).values_list('country', flat=True)
            context['countries'] = Country.objects.filter(id__in=set(country))
        elif 'country' in self.request.GET and 'edu-cat' in self.request.GET:
            country_id = self.request.GET['country']
            edu_cat_id = self.request.GET['edu-cat']
            context['educations'] = Education.objects.filter(country__pk=country_id, education_type__pk=edu_cat_id)

        return context

class ReserveSaveDateView(generic.FormView):
    template_name = "reserve/get_time_data.html"
    form_class = ContactUsForm

    def check_count(self, time):
        # time = str(times)
        settings = WebsiteSetings.objects.last()
        if settings.reservation_count:
            count = settings.reservation_count
        else:
            count = 5
        year, month, day = self.kwargs['year'], self.kwargs['month'], self.kwargs['day']
        current_time = str_join(year + "-" + month + "-" + day + " " + time + ":00")
        current_time_plus = str_join(year + "-" + month + "-" + day + " " + time + ":59")
        date_count = ReservationDate.objects.filter(date__gte=current_time, date__lte=current_time_plus).count()
        # selected_datetime = datetime.strptime(str(year) + ' ' + str(month) + ' ' + str(day) + ' ' + str(time) + ':00', '%Y-%m-%d %H:%M')
        if date_count < count:
            return True
        else:
            return False


    def get_context_data(self, **kwargs):
        context = super(ReserveSaveDateView, self).get_context_data(**kwargs)
        year, month, day = self.kwargs['year'], self.kwargs['month'], self.kwargs['day']
        # date_time = datetime.strptime(str(year) + '-' + str(month) + '-' + str(day), '%Y-%m-%d')
        if str(day) != datetime.now().strftime("%d"):
            context['reserve_count'] = date_range(str(year) + '-' + str(month) + '-' + str(day))
        else:
            current_date = datetime.now().date()
            current_time = datetime.now().time().strftime("%H")
            context['reserve_count'] = date_range(current_date, current_time)
        return context

    def form_valid(self, form):
        if self.request.POST.get('time', False):
            time = self.request.POST.get('time').strip()
            print(time)
            if self.check_count(str(time)):
                if self.request.is_ajax():
                    contact = form.save(commit=False)
                    contact.reference_url = self.request.POST.get("reference_url")
                    contact.save()
                    year, month, day = self.kwargs['year'], self.kwargs['month'], self.kwargs['day']
                    date_time = datetime.strptime(str_join(year, " ", month, " ", day, " ", time, ":00"),
                                                  '%Y %m %d %H:%M')
                    city = self.request.POST.get('city')
                    country_id = self.request.POST.get('country')
                    education_id = self.request.POST.get('education')

                    if country_id and education_id:
                        country = Country.objects.get(pk=country_id)
                        education = Education.objects.get(pk=education_id)
                        ReservationDate.objects.create(fk_id=contact.pk, date=date_time, country=country, education=education)
                    else:
                        ReservationDate.objects.create(fk_id=contact.pk, date=date_time)
                    return JsonResponse({
                        "save": True,
                        "message": "Müvəffəqiyyətlə yaradıldı"

                    })
            else:
                return JsonResponse({
                    "save": False,
                    "message": "Seçdiyiniz vaxta uyğun rezervasyon mümkün deyil!"
                })
        else:
            return JsonResponse({
                "save": False,
                "message": "Seçdiyiniz vaxt düzgün deyil!"
            })

    def form_invalid(self, form):
        return JsonResponse({
            "save": False,
            "message": form.errors
        })


def date_range(datetime, last_time=None):
    date_list = []
    for item in range(11, 20):
        if last_time is not None:
            if int(last_time) + 5 >= item:
                date_time = True
            else:
                date_time = False
        else:
            date_time = False
        current_time = str(item) + ":00"
        current_time_plus = str(item) + ":59"
        ctx = {"time": current_time,
               "count": ReservationDate.objects.filter(date__gte=str_join(datetime) + " " + current_time,
                                                       date__lte=str_join(datetime) + " " + current_time_plus).count(),
               "active": date_time}
        date_list.append(ctx)

    return date_list



def str_join(*args):
    return ''.join(map(str, args))



class ReserveSuccessfulView(generic.TemplateView):
    template_name = "reserve/done.html"


class InsuranceView(generic.TemplateView):
    template_name = "insurance/pasha-insurance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insurance'] = Insurance.objects.all().first()
        return context


# Error views
def error_404(request, exception):
    data = {}
    print(data)
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)



class faqView(generic.ListView):
    model = FaqQuestion
    template_name = "faq/faq.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        cover_image = WebsiteSetings.objects.filter().first().faq_cover_image
        if cover_image == None:
            cover_image = '/static/azeristudent/img/cover.jpg' 
        else:
            cover_image = cover_image
        context['coverUrl'] = cover_image.url

        return context 

