from django.contrib import admin
from .models import employee
from django.db import models



class employee(admin.ModelAdmin):
	fieldsets = [
          ("Content",{'fields':["firstname","lastname","emp_id"]}),
	  ]    


	admin.site.register(employee)

# Register your models here.
