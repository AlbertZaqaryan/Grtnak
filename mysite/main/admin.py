from django.contrib import admin
from .models import HomeName, HomeImage, Contact
# Register your models here.

@admin.register(HomeName)
class HomeNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'username']
    search_fields = ['username']


admin.site.register(HomeImage)