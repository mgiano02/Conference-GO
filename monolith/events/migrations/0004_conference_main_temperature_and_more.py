# Generated by Django 4.0.3 on 2023-03-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_location_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='main_temperature',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='conference',
            name='weather_description',
            field=models.TextField(null=True),
        ),
    ]