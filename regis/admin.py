from django.contrib import admin
from regis.models import database
# Register your models here.
class databaseAdmin(admin.ModelAdmin):
    list_display=['pk','first_name','last_name','email','password']
admin.site.register(database,databaseAdmin)