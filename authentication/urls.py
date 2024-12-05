from django.urls import path
from .views import *


urlpatterns = [

    path('',login),
    path('logout/', logout_user),
    path('signup/', signup)

]