# Generated by Django 5.1.1 on 2024-11-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landDetails", "0007_remove_landdetails_interested_buyer"),
    ]

    operations = [
        migrations.AddField(
            model_name="landdetails",
            name="length",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="landdetails",
            name="width",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
