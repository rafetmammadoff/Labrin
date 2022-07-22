from django import forms
from django.forms import formset_factory

from partners.models import RegisterFair, EventVideo, CitiesTables


class RegisterForm(forms.ModelForm):
    # cities = forms.ModelMultipleChoiceField(queryset=EventVideo.objects.filter(show_register=True),
    #                                         widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = RegisterFair
        fields = ['full_name', 'email', 'institution', 'message', 'billing_address', 'signature']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name', 'class': 'spring-form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': 'spring-form-input'}),
            'institution': forms.TextInput(attrs={'placeholder': 'Enter Institution name', 'class': 'spring-form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'spring-form-input textarea-form'}),
            'billing_address': forms.TextInput(attrs={'placeholder': 'Enter billing address', 'class': 'spring-form-input'}),
            'signature': forms.TextInput(attrs={'placeholder': 'Enter your signature', 'class': 'spring-form-input'}),
        }


class CitiesTableForm(forms.ModelForm):

    class Meta:
        model = CitiesTables
        fields = ['cities', 'table_count']
        widgets = {
            # 'table_count': forms.NumberInput(attrs={'class': 'nonform', 'disabled': 'disabled', 'min': 1})
            'table_count': forms.NumberInput(attrs={'class': 'amount', 'disabled': 'disabled', 'min': 1})
        }


CityFormSet = formset_factory(CitiesTableForm, extra=10)
