from django.forms import ModelForm
from .models import *
class Customer_form(ModelForm):
    class Meta():
        model=Customer
        fields='__all__'


class Orders_form(ModelForm):

    class Meta():

        model=Orders
        fields=['customer_reference','product_reference','order_number','order_date','quantity']       
