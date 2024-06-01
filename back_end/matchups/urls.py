from django.urls import path
from . import views

urlpatterns = [
    path("", views.matchups, name="matchups"),
    path("matchups_result/<int:pitcher_team_id>/<int:pitcher_player_id>/<int:batter_team_id>/<int:batter_player_id>/", 
         views.matchupsResult, name="matchups_result"),
    path("player_list/<str:kind>/<int:team_id>/", views.playerList, name="player_list"),
]
