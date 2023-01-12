from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'car_title', 'model', 'color', 'city', 'year', 'body_style', 'fuel_type', 'is_informed_buyer', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_informed_buyer', 'is_featured')
    
    def thumbnail(self, object): 
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Car Image'
    
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style')
    
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
    
admin.site.register(Car,CarAdmin)