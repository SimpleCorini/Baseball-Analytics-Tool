from django.db.models import Subquery, OuterRef
from .models import MasterTeam, RecordTeam, MasterPlayer
from .models import RecordTeamMatchup, RecommandPlayer, RecordBatterTeamMatchup
from .models import PredictionTeamMatch

def getTeam(team_id):
    try:
        team = MasterTeam.objects.get(pk=team_id)
    except:
        team = None
    return team

def getTeamList():
    teamList = MasterTeam.objects.all().order_by("team_name")
    return teamList

def getExcludeTeamList(team_id):
    teamList = MasterTeam.objects.exclude(pk=team_id).order_by("team_name")
    return teamList

def getRecordTeam(team_id):
    try:
        recordTeam = RecordTeam.objects.get(pk=team_id)
    except:
        recordTeam = None
    return recordTeam

def getRecordTeamMatchupList(team_id):
    recordTeamMatchupList = RecordTeamMatchup.objects.filter(pk=team_id).annotate(vs_team_name=Subquery(MasterTeam.objects.filter(team_id=OuterRef('vs_team_id')).values('team_name')))
    query = str(recordTeamMatchupList.query)
    return recordTeamMatchupList

def getRecordTeamMatchup(team_id, vs_team_id):
    try:
        recordTeamMatchup = RecordTeamMatchup.objects.annotate(vs_team_name=Subquery(MasterTeam.objects.filter(team_id=OuterRef('vs_team_id')).values('team_name'))).get(pk=team_id, vs_team_id=vs_team_id)
    except:
        recordTeamMatchup = None
    return recordTeamMatchup

def getPlayer(player_id):
    try:
        player = MasterPlayer.objects.get(player_id=player_id)
    except:
        player = None
    return player

def getTeamPlayerList(kind, team_id):
    try:
        if kind == 'P':         # 투수
            playerList = MasterPlayer.objects.filter(pk=team_id, position_no="P")
        else:                   # 타자
            playerList = MasterPlayer.objects.filter(pk=team_id).exclude(position_no="P")
    except:
        playerList = None
    return playerList

def getRecommandPlayerList(team_id):
    # recommandPlayerList = RecommandPlayer.objects.filter(pk=team_id)
    # recommandPlayerList = RecommandPlayer.objects.filter(pk=team_id).extra(tables=['master_player'], where=['recommand_player.player_id = master_player.player_id'],)
    recommandPlayerList = RecommandPlayer.objects.filter(pk=team_id).annotate(player_name=Subquery(MasterPlayer.objects.filter(player_id=OuterRef('player_id')).values('player_name')))
    query = str(recommandPlayerList.query)
    return recommandPlayerList

def getPredictionTeamMatch(team_id, vs_team_id):
    try:
        predictionTeamMatch = PredictionTeamMatch.objects.get(pk=team_id, vs_team_id=vs_team_id)
    except:
        predictionTeamMatch = None
    return predictionTeamMatch

def getRecordBatterTeamMatchup(player_id, vs_team_id):
    try:
        recordBatterTeamMatchup = RecordBatterTeamMatchup.objects.annotate(batter_player_name=Subquery(MasterPlayer.objects.filter(player_id=OuterRef('batter_player_id')).values('player_name'))).get(pk=player_id, vs_team_id=vs_team_id)
    except:
        recordBatterTeamMatchup = None
    return recordBatterTeamMatchup