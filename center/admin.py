from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'create')
    list_filter = ('title', 'status')
    search_fields = ('title', 'status')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create')
    list_filter = ('name', 'email', 'create')
    search_fields = ('name', 'email', 'create')