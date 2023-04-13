from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class FitUser(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    interest = models.TextField()
    goal = models.TextField()
    fitness_goal = models.CharField(max_length=50)
    current_plans = ArrayField(
        models.IntegerField(),
        size=3
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
    id = models.IntegerField()
    plan_name = models.TextField()
    description = models.TextField()
    difficulty_level = models.TextField()
    goal = models.TextField()
    equipment = models.TextField()
    training_part = models.TextField()