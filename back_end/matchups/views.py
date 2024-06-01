from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from baseball.views import getTeamList, getTeamPlayerList, getPlayer
from baseball.serializers import *

def matchups(request):
	teamList = getTeamList()
	context = {'team_list': teamList, }
	return render(request, "matchups/matchups.html", context)

def matchupsResult(request, pitcher_team_id, pitcher_player_id, batter_team_id, batter_player_id):
	pitcherPlayer = getPlayer(pitcher_player_id)
	batterPlayer = getPlayer(batter_player_id)
	context = {'pitcher_player': pitcherPlayer, 
			'batter_player': batterPlayer, 
			}
	return render(request, "matchups/matchups_result.html", context)

@api_view(['GET'])
def playerList(request, kind, team_id):
	playerList = getTeamPlayerList(kind, team_id)
	serializer = playerSerializer(playerList, many=True)
	return Response(serializer.data)