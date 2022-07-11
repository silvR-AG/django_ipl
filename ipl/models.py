from statistics import mode
from django.db import models
from django.contrib import admin

# Create your models here.


class matches(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    season = models.IntegerField(max_length=20, null=True)
    city = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    team1 = models.CharField(max_length=200, null=True)
    team2 = models.CharField(max_length=200, null=True)
    toss_winner = models.CharField(max_length=200, null=True)
    toss_decision = models.CharField(max_length=200, null=True)
    result = models.CharField(max_length=200, null=True)
    dl_applied = models.IntegerField(max_length=200, null=True)
    winner = models.CharField(max_length=200, null=True)
    win_by_runs = models.IntegerField(max_length=200, null=True)
    win_by_wickets = models.IntegerField(max_length=200, null=True)
    player_of_match = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=200, null=True)
    umpire1 = models.CharField(max_length=200, null=True)
    umpire2 = models.CharField(max_length=200, null=True)
    umpire3 = models.CharField(max_length=200, null=True)

class deliveries(models.Model):
    match_id = models.IntegerField()
    inning = models.CharField(max_length=200, null=True)
    batting_team = models.CharField(max_length=200, null=True)
    bowling_team = models.CharField(max_length=200, null=True)
    over = models.IntegerField(max_length=200, null=True)
    ball = models.IntegerField(max_length=200, null=True)
    batsman = models.CharField(max_length=200, null=True)
    non_striker = models.CharField(max_length=200, null=True)
    bowler = models.CharField(max_length=200, null=True)	
    is_super_over = models.IntegerField( null=True)	
    wide_runs = models.IntegerField(max_length=200, null=True)	
    bye_runs = models.IntegerField(max_length=200, null=True)	
    legbye_runs = models.IntegerField(max_length=200, null=True)	
    noball_runs = models.IntegerField(max_length=200, null=True)	
    penalty_runs = models.IntegerField(max_length=200, null=True)	
    batsman_runs = models.IntegerField(max_length=200, null=True)	
    extra_runs = models.IntegerField(max_length=200, null=True)	
    total_runs = models.IntegerField(max_length=200, null=True)	
    player_dismissed = models.CharField(max_length=200, null=True)	
    dismissal_kind = models.CharField(max_length=200, null=True)	
    fielder = models.CharField(max_length=200, null=True)

# class extra_runs(models.Model):
# class eco_bowl(models.Model):
