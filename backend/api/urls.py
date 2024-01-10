from django.urls import path
from .views import hello,home,login,register


urlpatterns = [
    
    path("hello/",hello),
    path("home",home),
    path("login/",login),
    path("register/",register),
]
