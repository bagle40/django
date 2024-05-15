from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.urls import reverse
from malling.forms import MailingForm


def malling(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index')) # Redirect to success page after subscription
        else:
            return HttpResponseRedirect(reverse('main:index'))
    else:
        return  MailingForm()