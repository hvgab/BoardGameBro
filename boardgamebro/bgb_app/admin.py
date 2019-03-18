from django.contrib import admin
from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['id', 'game', 'players_string']


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
