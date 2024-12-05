from django.urls import path
from .views import *

urlpatterns=[
    path('add/',customer_addpage),
    path('list/',customer_list),
    path('list/delete/,<int:id>/',customer_delete, name='delete'),
    path('list/update/,<int:id>/',customer_update, name='update'),
    path('add/a/',OrdersAdd),
    path('orders/',OrdersList),
    path('orders/delete/,<int:id>/',Ordersdelete, name='order_delete'),
    path('orders/updated/<int:id>/',orderupdate, name='orderupdate'),
    

]