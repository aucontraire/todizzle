from django.contrib import admin

from .models import Item, Tag


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['text']
    
    list_display = ('created', 'updated', 'completed', 'archived', 'text')
    
    list_filter = ['text']
    
admin.site.register(Item, ItemAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    list_display = ('created', 'name')

admin.site.register(Tag, TagAdmin)    
