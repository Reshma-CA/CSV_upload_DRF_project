from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from . models import *

class CSV_User(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')



admin.site.register(User,CSV_User)