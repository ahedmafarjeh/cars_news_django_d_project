# Generated by Django 4.1 on 2022-08-31 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_newstype_newstopic"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NewsTopic",
        ),
        migrations.DeleteModel(
            name="NewsType",
        ),
    ]
