from django.shortcuts import render
from django.views import View
from . import models
from . import forms

class HomePage(View):
    def get(self, req):
        context = {
            "faqs": models.FAQs.objects.filter(display = True)[:6],
            "itServices": models.ItServices.objects.filter(display = True),
            "ContactForm": forms.ContactForm()
        }

        return render(req, "main.html", context=context)
