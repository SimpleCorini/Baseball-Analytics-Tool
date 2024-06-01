from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from baseball.views import *
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def predictions(request):
	teamList = getTeamList()
	context = {'team_list': teamList, }        	
	return render(request, "predictions/predictions.html", context)

def predictionsResult(request, team_id, vs_team_id):
	predictionTeamMatch = getPredictionTeamMatch(team_id, vs_team_id)
	recordKeyPlayer = getRecordBatterTeamMatchup(predictionTeamMatch.key_player_id, vs_team_id)
	recordVsKeyPlayer = getRecordBatterTeamMatchup(predictionTeamMatch.vs_key_player_id, team_id)
	recordTeamMatchup = getRecordTeamMatchup(team_id, vs_team_id)
	team = getTeam(team_id);
	vsTeam = getTeam(vs_team_id);
	context = {'team': team, 
               'vs_team': vsTeam, 
			   'record_key_player': recordKeyPlayer,
			   'record_vs_key_player': recordVsKeyPlayer,
			   'record_team_matchup': recordTeamMatchup,
               'prediction_team_match': predictionTeamMatch, 
                }
	return render(request, "predictions/predictions_result.html", context)

@register.filter
def vs_win_rate(value):
    return 100 - value
