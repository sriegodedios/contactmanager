from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.

# register/
def index(req):
    #return HttpResponse('Registration Page Goes Here')
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Form Success!")
        else:
            return HttpResponse("Form Failed =(")
    else:
        form = RegisterForm()

        return render(req, 'register/index.html', {'form': form})

