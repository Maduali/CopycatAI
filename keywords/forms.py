from dataclasses import fields
from django import forms
from .models import Registration

class Registration_form1(forms.ModelForm):
    class Meta:

        model = Registration
        fields = ['name_of_organization','type_of_organization']
        widgets = {
            'type_of_organization': forms.RadioSelect
        }
        template_name = 'keywords/home.html'
class Registration_form2(forms.ModelForm):
    class Meta:

        model = Registration
        fields = ['admin_email', 'admin_whatsapp_number']
        template_name = 'keywords/home.html'
class Registration_form3(forms.ModelForm):
    class Meta:

        model = Registration
        fields = ['keywords','password']
        template_name = 'keywords/home.html'