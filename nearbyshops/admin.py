from django.contrib import admin
from djnago.contrib.gis.admin import OSMGeoAdmin
from .models import Shop


# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')