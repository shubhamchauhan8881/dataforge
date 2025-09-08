from django.shortcuts import render, redirect
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
    
    def post(self, req):

        form = forms.ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            context = {
            "faqs": models.FAQs.objects.filter(display = True)[:6],
            "itServices": models.ItServices.objects.filter(display = True),
            "ContactForm": form
            }
            return render(req, "main.html", context=context)