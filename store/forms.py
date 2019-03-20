from django import forms

from .models import Order, Product

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('recipient', 'address','creditCard')
        
class addForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('id', 'name','description', 'price')
