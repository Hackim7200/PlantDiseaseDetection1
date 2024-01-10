from django.urls import path
from .views import hello,login,register


urlpatterns = [
    
    path("hello/",hello),
    path("login/",login),
    path("register/",register),
]
