# Generated by Django 4.1.7 on 2023-04-13 22:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit_coach', '0002_alter_fituser_age_alter_fituser_fitness_goal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fituser',
            name='current_plans',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=3),
        ),
    ]
