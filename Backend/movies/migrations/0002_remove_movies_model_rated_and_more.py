# Generated by Django 5.1.5 on 2025-01-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies_model',
            name='rated',
        ),
        migrations.RemoveField(
            model_name='movies_model',
            name='realised_date',
        ),
        migrations.AddField(
            model_name='movies_model',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
    ]
