
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response({'res':'hello'})

@api_view(['GET'])
def home(request):
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
def register(req):
    return Response({'res':'hello'})

      
