from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import user

def login(request):

    context={
        'error':""
    }

    if request.method == 'POST':

        print(request.POST)

        user = authenticate(username = request.POST['username'], password = request.POST['password'])

        print(user)


        if user is not None:
            pass

            #login( request , user)

            return redirect('order/list/')
        
        else:
            context={
                "error":'**invalid Username or password'
            }
            return render(request, 'login.html', context)
        

    return render (request,'login.html',context)


def logout_user(request):

    logout(request)

    return redirect('/')
def signup(request):
    context={
        'error':""
    }
    if request.method=='POST':
        user_check=user.objects.filter(username=request.POST['username'])
        if len(user_check) > 0:
            context={
                'error':'**already username exist!!!'
            }
            return render(request,'signup.html',context)



        else:    


            new_user = user(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],
                            email=request.POST['email'],age=request.POST['age'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/')

    return render(request,'signup.html',context)