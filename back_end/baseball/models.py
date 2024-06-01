# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MasterPlayer(models.Model):
    player_id = models.CharField(max_length=20, db_comment='선수 ID')
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')  # The composite primary key (team_id, player_id) found, that is not supported. The first column is selected.
    player_name = models.CharField(max_length=100, db_comment='선수 명')
    position = models.CharField(max_length=20, db_comment='포지션')
    position_no = models.CharField(max_length=2, db_comment='포지션 번호')
    game_count = models.IntegerField(db_comment='경기 수')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'master_player'
        unique_together = (('team_id', 'player_id'),)
        db_table_comment = '선수 마스터'


class MasterTeam(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')
    team_name = models.CharField(max_length=100, db_comment='팀 명')
    team_alias = models.CharField(max_length=100, db_comment='팀 별명')
    image_data = models.CharField(max_length=10000, blank=True, null=True, db_comment='이미지 데이터')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'master_team'
        db_table_comment = '팀 마스터'


class PredictionTeamMatch(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')  # The composite primary key (team_id, vs_team_id) found, that is not supported. The first column is selected.
    vs_team_id = models.CharField(max_length=20, db_comment='상대 팀 ID')
    prediction_win_rate = models.FloatField(db_comment='예측 승률')
    key_player_id = models.CharField(max_length=20, db_comment='키 선수 ID')
    vs_key_player_id = models.CharField(max_length=20, db_comment='상대 키 선수 ID')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'prediction_team_match'
        unique_together = (('team_id', 'vs_team_id'),)
        db_table_comment = '팀 대결 예측'


class RecordBatter(models.Model):
    player_id = models.CharField(primary_key=True, max_length=20, db_comment='선수 ID')
    batting_avg = models.FloatField(db_comment='타율')
    hits = models.IntegerField(db_comment='안타')
    hr = models.IntegerField(db_comment='홈런 수')
    rbi = models.IntegerField(db_comment='타점')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_batter'
        db_table_comment = '타자 기록'


class RecordBatterTeamMatchup(models.Model):
    batter_player_id = models.CharField(primary_key=True, max_length=20, db_comment='타자 선수 ID')  # The composite primary key (batter_player_id, vs_team_id) found, that is not supported. The first column is selected.
    vs_team_id = models.CharField(max_length=20, db_comment='상대 팀 ID')
    batting_avg = models.FloatField(db_comment='타율')
    hits = models.IntegerField(db_comment='안타')
    hr = models.IntegerField(db_comment='홈런')
    rbi = models.IntegerField(db_comment='타점')
    recent_batting_avg = models.FloatField(db_comment='최근 타율')
    recent_hits = models.IntegerField(db_comment='최근 안타')
    recent_hr = models.IntegerField(db_comment='최근 홈런')
    recent_rbi = models.IntegerField(db_comment='최근 타점')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_batter_team_matchup'
        unique_together = (('batter_player_id', 'vs_team_id'),)
        db_table_comment = '타자 팀별 대결 기록'


class RecordPitcher(models.Model):
    player_id = models.CharField(primary_key=True, max_length=20, db_comment='선수 ID')
    win_count = models.IntegerField(db_comment='승 수')
    lose_count = models.IntegerField(db_comment='패 수')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_pitcher'
        db_table_comment = '투수 기록'


class RecordPlayerMatchup(models.Model):
    batter_player_id = models.CharField(primary_key=True, max_length=20, db_comment='타자 선수 ID')  # The composite primary key (batter_player_id, pitcher_player_id) found, that is not supported. The first column is selected.
    pitcher_player_id = models.CharField(max_length=20, db_comment='투수 선수 ID')
    game_date = models.DateField(db_comment='경기 일자')
    pa = models.FloatField()
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_player_matchup'
        unique_together = (('batter_player_id', 'pitcher_player_id'),)
        db_table_comment = '타자 투수 대결 기록'


class RecordTeam(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')
    ranking = models.IntegerField(db_comment='순위')
    win = models.IntegerField(db_comment='승')
    draw = models.IntegerField(db_comment='무')
    lose = models.IntegerField(db_comment='패')
    war = models.FloatField(db_comment='승리 기여도')
    batting_avg = models.FloatField(db_comment='타율')
    batting_avg_ranking = models.IntegerField(db_comment='타율 순위')
    brraa = models.FloatField(db_comment='주루')
    brraa_ranking = models.IntegerField(db_comment='주루 순위')
    waa_pos = models.FloatField(db_comment='수비')
    waa_pos_ranking = models.IntegerField(db_comment='수비 순위')
    starter_war = models.FloatField(db_comment='선발')
    starter_war_ranking = models.IntegerField(db_comment='선발 순위')
    relief_war = models.FloatField(db_comment='구원')
    relief_war_ranking = models.IntegerField(db_comment='구원 순위')
    waa_bt = models.FloatField(db_comment='(야수) 타격 승리 기여도')
    waa_sb = models.FloatField(db_comment='(야수) 도루 승리 기여도')
    waa_br = models.FloatField(db_comment='(야수) 주루 승리 기여도')
    waa_def = models.FloatField(db_comment='(야수) 수비 승리 기여도')
    rep_wins = models.FloatField(db_comment='(야수) 대체 승리')
    waa_gs = models.FloatField(db_comment='(투수) 선발 승리 기여도')
    waa_gr = models.FloatField(db_comment='(투수) 구원 승리 기여도')
    rep_wins_gs = models.FloatField(db_comment='(투수) 대체 선발 승리 기여도')
    rep_wins_gr = models.FloatField(db_comment='(투수) 대체 구원 승리 기여도')
    war_gs = models.FloatField(db_comment='(투수) 선발 승리 기여도')
    war_gr = models.FloatField(db_comment='(투수) 구원 승리 기여도')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_team'
        db_table_comment = '팀 기록'


class RecordTeamMatchup(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')  # The composite primary key (team_id, vs_team_id) found, that is not supported. The first column is selected.
    vs_team_id = models.CharField(max_length=20, db_comment='상대 팀 ID')
    win = models.IntegerField(db_comment='승')
    draw = models.IntegerField(db_comment='무')
    lose = models.IntegerField(db_comment='패')
    win_rate = models.FloatField(db_comment='승율')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'record_team_matchup'
        unique_together = (('team_id', 'vs_team_id'),)
        db_table_comment = '팀 기록'


class RecommandPlayer(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20, db_comment='팀 ID')  # The composite primary key (team_id, position_no) found, that is not supported. The first column is selected.
    position_no = models.CharField(max_length=2, db_comment='포지션 번호')
    player_id = models.CharField(max_length=20, db_comment='선수 ID')
    last_update_datetime = models.DateTimeField(db_comment='최종 수정 일시')

    class Meta:
        managed = False
        db_table = 'recommand_player'
        unique_together = (('team_id', 'position_no'),)
        db_table_comment = '추천 선수'
