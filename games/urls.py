from django.urls import path

from .views import show_games, show_game

urlpatterns = [
    path('', show_games),
    path('game/<int:game_id>/', show_game),
]
