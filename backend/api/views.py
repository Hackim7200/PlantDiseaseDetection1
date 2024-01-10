from django.http import HttpResponse

# Create your views here.

def hello(req):
    return HttpResponse("Hello")

def home(req):
    return HttpResponse("Home")
    
def login(req):
    return HttpResponse("login")

def register(req):
    return HttpResponse("register")
