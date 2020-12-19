from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
