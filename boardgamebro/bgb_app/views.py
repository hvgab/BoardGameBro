from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Player, Play, Game
from .forms import PlayForm
from django.db.models import Count, Q


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # MOST PLAYED GAME
        most_played_game = Game.objects.annotate(Count(
            'play', distinct=True)).order_by('-play__count').first()
        print(most_played_game)
        context['most_played_game'] = most_played_game

        # PLAYER WITH MOST PLAYS
        player_most_plays = Player.objects.annotate(
            Count('play', distinct=True)).order_by('-play__count').first()
        print((player_most_plays))
        context['player_most_plays'] = player_most_plays

        return context


# PLAYER
class PlayerListView(ListView):
    model = Player
    template_name = 'bgb_app/player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # WIN COUNT
        # players = Player.objects.annotate(Count(
        #     'games', distinct=True)).annotate(
        #         win__count=Count(
        #             'play', distinct=True, filter=Q(
        #                 play__winner__id=id))).all()

        return context


class PlayerDetailView(DetailView):
    model = Player

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
    template_name = 'bgb_app/game_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detail_view'] = 'bgb:game-detail'
    #     context['fields'] = [
    #         field.name for field in self.model._meta.get_fields()
    #     ]
    #     return context

    def get_queryset(self):
        queryset = Game.objects.annotate(
            Count('play', distinct=True)).annotate(
                Count('player', distinct=True)).all()

        # for row in queryset:
        #     print(row.__dict__)
        return queryset


class GameDetailView(DetailView):
    model = Game
    template_name = 'bgb_app/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


# PLAY
class PlayListView(ListView):
    model = Play

    # template_name = 'bgb_app/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_view'] = 'bgb:play-detail'
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


class PlayDetailView(DetailView):
    model = Play
    template_name = 'bgb_app/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


class PlayCreateView(CreateView):
    model = Play
    fields = '__all__'


# def add_play(request):
#     if request.method == 'POST':
#         form = PlayForm(request.POST)
#         if form.is_valid():
#             messages.success('Play added!')
#             return redirect(add_play)
#
#     else:
#         form = PlayForm()
#
#     return render(request, 'add_play.html', {'form': form})

# def player(request, pk):
#     player = get_object_or_404(Player, id=pk)
#     winrate = player.get_winrate()
#     return render(
#         request,
#         'player.html',
#         context=dict(player=player, winrate=winrate, winpercent=winrate * 100))
