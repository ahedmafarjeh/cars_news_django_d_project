# Generated by Django 4.1 on 2022-08-25 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="piece",
            old_name="piece_car_model",
            new_name="car_id",
        ),
    ]
