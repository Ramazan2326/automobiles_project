from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import Car

class carsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Car, carsAdmin)

# Register your models here.
