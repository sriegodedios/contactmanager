from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    #return HttpResponse('Registration Page Goes Here')
    return render(req, 'register/index.html')