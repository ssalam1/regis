from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.forms import ModelForm
from regis.models import *
from django.core.context_processors import csrf
# Create your views here.
def index(request):
    if request.POST:
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<html><h1>Done!</h1></html>")
    else:
        form=register_form()
            
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('index.html',args)
