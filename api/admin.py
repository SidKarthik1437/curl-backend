from django.contrib import admin

# Register your models here.
from .models import Script
from .models import File

admin.site.register(Script)
admin.site.register(File)