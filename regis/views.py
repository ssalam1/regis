from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.forms import ModelForm
from regis.models import *
# Create your views here.
def index(request):
    newuser=database()
    if request.method=="GET":
        form=register_form()
        return render(request,'index.html',{'form':form})
    elif request.method=="POST":
        newuser.first_name=request.POST['first_name']
        newuser.last_name=request.POST['last_name']
        newuser.email=request.POST['email']
        newuser.password=request.POST['password']
        newuser.save()
        return HttpResponse("<html><h1>Done!</h1></html>")
