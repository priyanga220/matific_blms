# Generated by Django 5.0.6 on 2024-06-19 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_team_teamname_team_teamslogan_team_updateddate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="updatedDate",
            new_name="created_date",
        ),
        migrations.RenameField(
            model_name="team",
            old_name="teamName",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="team",
            old_name="teamSlogan",
            new_name="slogan",
        ),
    ]
