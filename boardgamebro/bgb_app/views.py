from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Player, Play, Game
from .forms import PlayForm


class HomeView(TemplateView):
    template_name = 'home.html'


# PLAYER
class PlayerListView(ListView):
    model = Player
    template_name = 'bgb_app/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_view'] = 'bgb:player-detail'
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


class PlayerDetailView(DetailView):
    model = Player


# GAME
class GameListView(ListView):
    model = Game
    template_name = 'bgb_app/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_view'] = 'bgb:game-detail'
        context['fields'] = [
            field.name for field in self.model._meta.get_fields()
        ]
        return context


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
    template_name = 'bgb_app/generic_list.html'

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
