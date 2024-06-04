from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Enquiry

class Enquiry(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('Name', 'Level', 'Course', 'Preferred_Timing', 'Contact',)


    def clean_level(self):
        data = self.cleaned_data.get('Name')
    
    def clean_Level(self):
        data = self.cleaned_data.get('Level')
    
    def clean_Course(self):
        data = self.cleaned_data.get('Course')
    
    def clean_Preferred_Timing(self):
        data = self.cleaned_data.get('Preferred_Timing')

    def clean_Contact(self):
        data = self.cleaned_data.get('Contact')

