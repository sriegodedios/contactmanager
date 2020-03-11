from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.

# register/
def index(req):
    #return HttpResponse('Registration Page Goes Here')
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        print(form.Meta)


        if form.is_valid():
            new_form = form.save()
            return HttpResponse("Form Success!")

        messages.error(req, "Please correct the error(s) below.")
        return render(req, 'register/index.html', {'form': form})
    else:
        form = RegisterForm()

        return render(req, 'register/index.html', {'form': form})

