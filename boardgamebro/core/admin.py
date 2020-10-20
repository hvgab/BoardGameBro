from django.contrib import admin
from .models import *


class GameInline(admin.TabularInline):
    model = Game

class GamenightInline(admin.TabularInline):
    model = Gamenight

class LocationInline(admin.TabularInline):
    model = Location

class PlaythroughInlineAdmin(admin.TabularInline):
    model = Playthrough
class PlayerInline(admin.TabularInline):
    model = Player

class ScoreInline(admin.TabularInline):
    model = Score

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']

@admin.register(Gamenight)
class GamenightAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']
    inlines = [PlaythroughInlineAdmin]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '__str__']

@admin.register(Playthrough)
class PlaythroughAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'game', 'players_string']
    inlines = [ScoreInline]

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass