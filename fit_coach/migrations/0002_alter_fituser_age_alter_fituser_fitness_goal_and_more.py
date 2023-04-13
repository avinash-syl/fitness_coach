# Generated by Django 4.1.7 on 2023-04-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit_coach', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fituser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='fitness_goal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='goal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='interest',
            field=models.TextField(blank=True, null=True),
        ),
    ]