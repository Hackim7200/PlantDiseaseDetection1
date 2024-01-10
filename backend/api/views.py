
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib import messages 
#contrib are premade classes for defualt use

#auth
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response({'res':'hello'})


@api_view(['POST'])
def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    
    return Response({
        "email":email,
        "password":password,
    })

@api_view(['POST'])
def register(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    
    user = User.objects.create_user(username,email,password)
    
    messages.success(request,"you account is created")
    
    return Response({'res':'hello'})

      
