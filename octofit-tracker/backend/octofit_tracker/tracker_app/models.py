from djongo import models
from djongo.models import ObjectIdField
from bson import ObjectId

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'tracker_app'

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()

    class Meta:
        app_label = 'tracker_app'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

    class Meta:
        app_label = 'tracker_app'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        app_label = 'tracker_app'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'tracker_app'
