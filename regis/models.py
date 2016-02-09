from django.db import models

# Create your models here.
class database(models.Model):
    first_name=models.CharField(max_length=255,blank=False,null=False)
    last_name=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)