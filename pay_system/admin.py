from django.contrib import admin

from pay_system.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') 
    search_fields = ['name']
