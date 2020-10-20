from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Player, Playthrough, Game
from ..forms import PlaythroughForm, MiniPlaythroughForm
from django.db.models import Count, Q


class PlaythroughForm(TemplateView):
    template_name = 'playthrough_form.html'


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # MOST PLAYED GAME 
        # most_played_game = Game.objects.annotate(Count(
            # 'playthrough', distinct=True)).order_by('-playthrough__count').first()
        # print(most_played_game)
        # context['most_played_game'] = most_played_game

        # PLAYER WITH MOST PLAYS
        # player_most_plays = Player.objects.annotate(
        #     Count('playthrough', distinct=True)).order_by('-playthrough__count').first()
        # print((player_most_plays))
        # context['player_most_plays'] = player_most_plays

        # return context


# PLAYER
class PlayerListView(ListView):
    model = Player
    template_name = 'core/player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # WIN COUNT
        # players = Player.objects.annotate(Count(
        #     'games', distinct=True)).annotate(
        #         win__count=Count(
        #             'playthrough', distinct=True, filter=Q(
        #                 playthrough__winner__id=id))).all()

        return context


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'core/player_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('context:')
        print(context)

        # MOST PLAYED GAME
        context['most_played_game'] = dict()
        game = context['object'].get_most_played_game()
        context['most_played_game']['game'] = game
        winrate = context['object'].get_winpercent(game)
        context['most_played_game']['winrate'] = winrate

        # MOST PLAYED PLAYER
        context['most_played_player'] = dict()
        player = context['object'].get_most_played_player()
        context['most_played_player']['player'] = player
        winrate = context['object'].get_winpercent(player=player)
        context['most_played_player']['winrate'] = winrate

        return context


# GAME
class GameListView(ListView):
    model = Game
    template_name = 'core/game_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detail_view'] = 'bgb:game-detail'
    #     context['fields'] = [
    #         field.name for field in self.model._meta.get_fields()
    #     ]
    #     return context

    def get_queryset(self):
        queryset = Game.objects.annotate(
            Count('playthrough', distinct=True)).annotate(
                Count('player', distinct=True)).all()

        # for row in queryset:
        #     print(row.__dict__)
        return queryset


class GameDetailView(DetailView):
    model = Game
    template_name = 'core/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


# Playthrough ( one playthroug of a game )
class PlaythroughListView(ListView):
    model = Playthrough

    # template_name = 'core/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_view'] = 'bgb:playthrough-detail'
        context['fields'] = [
            field.name for field in self.Playthrough._meta.get_fields()
        ]
        context['form'] = MiniPlaythroughForm
        return context


class PlaythroughDetailView(DetailView):
    model = Playthrough
    # template_name = 'core/generic_detail.html'
    template_name = 'core/playthrough_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            field.name for field in self.Playthrough._meta.get_fields()
        ]
        return context


class PlaythroughCreateView(CreateView):
    model = Playthrough
    fields = '__all__'


class PlaythroughUpdateView(UpdateView):
    model = Playthrough
    fields = '__all__'
