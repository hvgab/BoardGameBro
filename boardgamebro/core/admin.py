from django.contrib import admin
from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']

@admin.register(Gamenight)
class GamenightAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'game', 'players_string']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass