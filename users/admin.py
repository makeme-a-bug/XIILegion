from django.contrib import admin
from .models import roles,color
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(roles)
admin.site.register(color)
