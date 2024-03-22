from django import forms

from orders.models import Order

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','phone_number','delivery_address','payment_on_get','coment_order']
    
    
    
    first_name=forms.CharField()
    last_name=forms.CharField()
    phone_number=forms.CharField()
    delivery_address=forms.CharField()
    payment_on_get=forms.ChoiceField(choices=[("0", 'False'),("1", 'True'),],)
    coment_order= forms.CharField(required=False)
    
