from django.shortcuts import render,redirect
from .forms import *
from .models import *



def products(request):
    context={
        'product_form' : Product_Form()
    }
    if request.method=="POST":
        product_form = Product_Form(request.POST)

        if product_form.is_valid():

            product_form.save()

    return render(request, 'product.html',context)
def add_product(request):
    text={
        "all_product": product.objects.all()
    }
    return render(request,'product_add.html',text)
def delete_product(request,id):
    selected_product= product.objects.get(id=id)
    selected_product.delete()
    return redirect('/inventory/products/add/')

def update_product(request,id):
    selected_product=product.objects.get(id = id)
    context={
    'product_form':Product_Form(instance=selected_product)
    }
    if request.method=="POST":
        product_form = Product_Form(request.POST,instance=selected_product)

        if product_form.is_valid():

            product_form.save()
            return redirect('/inventory/products/add/')
    

    return render(request,'product.html',context)



    


