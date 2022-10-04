from django.contrib import admin

from .models import library,logs
# Register your models here.

admin.site.register(library)
admin.site.register(logs)