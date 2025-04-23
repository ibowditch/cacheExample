from django.db import models

# Create your models here.

class Game(models.Model):
    fixture_date = models.DateField()
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
