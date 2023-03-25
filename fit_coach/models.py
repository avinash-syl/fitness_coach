from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    difficulty_level = models.IntegerField()
    
    
class Exercise(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    target_muscles = models.TextField()