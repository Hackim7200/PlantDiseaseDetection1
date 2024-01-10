from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response({'res':'hello'})

@api_view(['GET'])
def home(request):
    return Response({'res':'hello'})

@api_view(['GET'])
def login(request):
    return Response({'res':'hello'})

@api_view(['GET'])
def register(req):
    return Response({'res':'hello'})

      
