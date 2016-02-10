from django.db import models
from django import forms
# Create your models here.
class database(models.Model):
    first_name=models.CharField(max_length=255,blank=False,null=False)
    last_name=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

    
class register_form(forms.ModelForm):
    class Meta:
        model=database
        fields=['first_name','last_name','email','password']