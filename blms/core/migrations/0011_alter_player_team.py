# Generated by Django 5.0.6 on 2024-06-21 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_remove_coach_team_team_coach"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="players",
                to="core.team",
            ),
        ),
    ]
