# Generated by Django 5.0 on 2023-12-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshitapp', '0002_earthquake_flood_glof_landslide_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
