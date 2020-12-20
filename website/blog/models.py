from django.db import models
from django.contrib.auth.models import User


class League(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()

    def __str__(self):
        return self.name

    def priority(nWins: int, nLosses: int, nDraws: int, g_for: int, g_against:int):
        gd = g_for - g_against
        return (nWins*3) + draws - (nLosses*3) + (0.25*gd)


class UserTeams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__() + ": " + self.team.__str__()
