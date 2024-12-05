from django.shortcuts import render,redirect
from .forms import *
from .models import *

def customer_addpage(request):
    context={
        'customer_form' : Customer_form()

    }
    if request.method == 'POST':
        customer_form = Customer_form(request.POST) 

        if customer_form.is_valid():

            customer_form.save()

    
    return render(request,'customer_add.html',context)

def customer_list(request):
    context={
    'all_customer':Customer.objects.all()
    }

    return render(request,'customer_list.html',context)
def customer_delete(request,id):
    selected_customer = Customer.objects.get(id=id)
    selected_customer.delete()
    return redirect('/order/list/')
def customer_update(request,id):
    selected_customer=Customer.objects.get(id = id)
    context={
    'customer_form':Customer_form(instance=selected_customer)
    }

    if request.method=='POST':

        customer_form=Customer_form(request.POST,instance=selected_customer)

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/order/list/')


    return render(request,'customer_add.html',context)

def OrdersAdd(request):
    context={
        'order_form' : Orders_form()
    }
    if request.method == 'POST':
        selected_product=product.objects.get(id=request.POST['product_reference'])

        amount=float(selected_product.price) * float(request.POST['quantity'])

        gst_amount=(amount*selected_product.gst) / 100

        bill_amount= amount + gst_amount
        new_order=Orders(customer_reference_id = request.POST['customer_reference'],product_reference_id=request.POST['product_reference'],order_number= request.POST['order_number'],order_date=request.POST['order_date'],amount=amount,gst_amount=gst_amount,bill_amount=bill_amount)
        new_order.save()
        return redirect ('/order/orders/')
    return render(request,'order.html',context)

def OrdersList(request):

    context={
        'all_orders':Orders.objects.all()
    }
    return render(request,'order_add.html',context)

def Ordersdelete(request,id):
    order=Orders.objects.get(id=id)

    order.delete()
    return redirect('/order/orders/')

def orderupdate(request, id):
    orders=Orders.objects.get(id = id)

    context={
        'order_form': Orders_form(instance=orders)
        
    }
    if request.method=='POST':
        selected_product=product.objects.get(id=request.POST['product_reference'])

        amount=float(selected_product.price) * float(request.POST['quantity'])

        gst_amount=(amount*selected_product.gst) / 100

        bill_amount= amount + gst_amount
        order_filter = Orders.objects.filter(id=id)
        order_filter.update(customer_reference_id = request.POST['customer_reference'],product_reference_id=request.POST['product_reference'],order_number= request.POST['order_number'],order_date=request.POST['order_date'],amount=amount,gst_amount=gst_amount,bill_amount=bill_amount)

        return redirect('/order/orders')

    return render(request,'order.html',context)





