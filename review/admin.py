from django.contrib import admin

# Register your models here.
from .models import cinemareview

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','rate','review','created_date',)
    list_display_links = ('nickname','rate','review','created_date',)

admin.site.register(cinemareview,PostAdmin)