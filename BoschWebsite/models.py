import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

# Saving Data of a Team
class Team(models.Model):
    name_text = models.CharField(max_length=50)
    symbol = models.CharField(max_length=300)
    wins = models.IntegerField(default=0)
    poles = models.IntegerField(default=0)
    titles = models.IntegerField(default=0)
    titles_drivers = models.IntegerField(default=0)
    titles_constructors = models.IntegerField(default=0)
    boss = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    boss_image = models.CharField(max_length=300, default=0)

    # Instead of showing Team (1) in shell now it shows e.g. Team McLaren
    # Same in admin website when Deleting (http://127.0.0.1:8000/admin/)
    def __str__(self):
        return self.name_text


class Driver(models.Model):
    name_text = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default="", null=True, blank=True)
    age = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    poles = models.IntegerField(default=0)
    titles = models.IntegerField(default=0)
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    driver_image = models.CharField(max_length=300)

    # Instead of showing Driver (1) in shell now it shows e.g. Driver Lando Norris
    # Same in admin website when Deleting (http://127.0.0.1:8000/admin/)
    def __str__(self):
        return self.name_text


# Saving Data of a Track
class Track(models.Model):
    name_text = models.CharField(max_length=50)
    laps = models.IntegerField(default=0)
    lapRecord = models.TimeField()
    sector1 = models.TimeField()
    sector2 = models.TimeField()
    sector3 = models.TimeField()
    length = models.FloatField(default=0)
    layout = models.CharField(max_length=300)

    # Instead of showing Track (1) in shell now it shows e.g. Track Melbourne
    # Same in admin website when Deleting (http://127.0.0.1:8000/admin/)
    def __str__(self):
        return self.name_text
