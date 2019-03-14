from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Game)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['id', 'players_string']
