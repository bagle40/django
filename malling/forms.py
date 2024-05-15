from django import forms
from malling.models import Mailing




class MailingForm(forms.ModelForm):
    class Meta:
        model=Mailing
        fields=['e_mail']

    e_mail=forms.CharField()