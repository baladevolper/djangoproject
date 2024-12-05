from django.urls import path
from .views import *

urlpatterns=[
    path('products/', products),
    path('products/add/', add_product),
    path('products/update/<int:id>/', update_product, name='updated'),
    path('products/delete/<int:id>/', delete_product, name='deleted'),
    
    

]
