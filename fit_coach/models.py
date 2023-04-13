from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class FitUser(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    interest = models.TextField(null=True, blank=True)
    goal = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=50)
    fitness_goal = models.TextField(null=True, blank=True)
    current_plans = ArrayField(
        models.IntegerField(),
        size=3,
        default=list
    )
    rating = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    def __init__(self, username, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_id = uuid.uuid4()
        self.username = username
    
class WorkoutPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    plan_name = models.TextField()
    description = models.TextField()
    difficulty_level = models.TextField()
    goal = models.TextField()
    equipment = models.TextField()
    training_part = models.TextField()