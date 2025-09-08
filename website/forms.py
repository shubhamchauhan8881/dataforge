from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.UserQueries
        fields = '__all__'