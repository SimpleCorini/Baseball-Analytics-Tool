from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from baseball.views import getExcludeTeamList, getTeam, getRecordTeam, getRecordTeamMatchupList, getRecommandPlayerList

def analysis(request):
	return render(request, "analysis/analysis.html")

def analysisTeam(request, id):
    team = getTeam(id)
    teamList = getExcludeTeamList(id)
    recordTeam = getRecordTeam(id)
    recordTeamMatchupList = getRecordTeamMatchupList(id)
    recommandPlayerList = getRecommandPlayerList(id)
    context = {'team': team, 
               'team_list': teamList,
               'record_team': recordTeam,
               'record_team_matchup_list': recordTeamMatchupList,
               'recommand_player_list': recommandPlayerList,
                }        
    return render(request, "analysis/analysis_team.html", context)