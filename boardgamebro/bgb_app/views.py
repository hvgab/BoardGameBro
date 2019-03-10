from django.shortcuts import render, get_object_or_404
from .models import Player


# Create your views here.
def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    winrate = player.get_winrate()
    return render(
        request,
        'player.html',
        context=dict(player=player, winrate=winrate, winpercent=winrate * 100))
