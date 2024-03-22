
from django.shortcuts import  render,redirect
from goods.models import Categories, Products


from django.http import HttpResponseRedirect
from django.urls import reverse

from main.forms import ContactForm,MailingForm
from main.models import Contact,Mailing


def index(request):

    goods=Products.objects.all()[:3]
    
    if request.method=='POST':
        form=MailingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form=MailingForm()

    context= {
        'title':'Norda - Главная',
        'goods':goods,
        'form':form
    }

    return render(request, 'main/index.html',context)


def about(request):
    context={
        'title':'Norda - О нас',
        'sub_title' :'О нас',
    }
    return render(request,'main/about.html',context)


def contact(request):
    if request.method=='POST':
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form=ContactForm()

    context={
        'title':'Norda - Контакты',
        'sub_title' :'Контакты',
        'form':form
    }
    return render(request,'main/contact.html',context)
