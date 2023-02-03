from django.shortcuts import render

from .models import Games

# Create your views here.

def show_games(request):
    games = Games.objects.all()
    
    return render(request, "games/index.html", {'games': games})


def show_game(request, game_id):
    game = Games.objects.get(id=game_id)
    
    return render(request, "games/game.html", {'game': game})
