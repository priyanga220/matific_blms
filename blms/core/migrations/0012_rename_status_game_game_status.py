# Generated by Django 5.0.6 on 2024-06-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_player_team"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="status",
            new_name="game_status",
        ),
    ]