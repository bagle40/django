from django import forms

from main.models import Contact
from main.models import Mailing


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['username','e_mail','subject','coment_text']

    username=forms.CharField()
    e_mail=forms.CharField()
    subject=forms.CharField()
    coment_text=forms.CharField()



class MailingForm(forms.ModelForm):
    class Meta:
        model=Mailing
        fields=['e_mail']

    e_mail=forms.CharField()
