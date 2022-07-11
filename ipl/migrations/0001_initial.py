# Generated by Django 4.0.6 on 2022-07-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('inning', models.CharField(max_length=200, null=True)),
                ('batting_team', models.CharField(max_length=200, null=True)),
                ('bowling_team', models.CharField(max_length=200, null=True)),
                ('over', models.IntegerField(max_length=200, null=True)),
                ('ball', models.IntegerField(max_length=200, null=True)),
                ('batsman', models.CharField(max_length=200, null=True)),
                ('non_striker', models.CharField(max_length=200, null=True)),
                ('bowler', models.CharField(max_length=200, null=True)),
                ('is_super_over', models.IntegerField(null=True)),
                ('wide_runs', models.IntegerField(max_length=200, null=True)),
                ('bye_runs', models.IntegerField(max_length=200, null=True)),
                ('legbye_runs', models.IntegerField(max_length=200, null=True)),
                ('noball_runs', models.IntegerField(max_length=200, null=True)),
                ('penalty_runs', models.IntegerField(max_length=200, null=True)),
                ('batsman_runs', models.IntegerField(max_length=200, null=True)),
                ('extra_runs', models.IntegerField(max_length=200, null=True)),
                ('total_runs', models.IntegerField(max_length=200, null=True)),
                ('player_dismissed', models.CharField(max_length=200, null=True)),
                ('dismissal_kind', models.CharField(max_length=200, null=True)),
                ('fielder', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='matches',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('season', models.IntegerField(max_length=20, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('team1', models.CharField(max_length=200, null=True)),
                ('team2', models.CharField(max_length=200, null=True)),
                ('toss_winner', models.CharField(max_length=200, null=True)),
                ('toss_decision', models.CharField(max_length=200, null=True)),
                ('result', models.CharField(max_length=200, null=True)),
                ('dl_applied', models.IntegerField(max_length=200, null=True)),
                ('winner', models.CharField(max_length=200, null=True)),
                ('win_by_runs', models.IntegerField(max_length=200, null=True)),
                ('win_by_wickets', models.IntegerField(max_length=200, null=True)),
                ('player_of_match', models.CharField(max_length=200, null=True)),
                ('venue', models.CharField(max_length=200, null=True)),
                ('umpire1', models.CharField(max_length=200, null=True)),
                ('umpire2', models.CharField(max_length=200, null=True)),
                ('umpire3', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
