# Generated by Django 5.0 on 2023-12-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earthquake',
            fields=[
                ('earthquake_key', models.AutoField(primary_key=True, serialize=False)),
                ('richter', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('casualties', models.IntegerField(blank=True, null=True)),
                ('loss', models.IntegerField(blank=True, null=True)),
                ('latitude_epicenter', models.FloatField(blank=True, null=True)),
                ('longitude_epicenter', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flood',
            fields=[
                ('flood_key', models.AutoField(primary_key=True, serialize=False)),
                ('rainfall', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('casualties', models.IntegerField(blank=True, null=True)),
                ('loss', models.IntegerField(blank=True, null=True)),
                ('latitude_epicenter', models.FloatField(blank=True, null=True)),
                ('longitude_epicenter', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('cause', models.CharField(choices=[('rainfall', 'Rainfall'), ('landslide', 'Landslide'), ('golf', 'Golf'), ('dam_failure', 'Dam Failure'), ('river_channel_changes', 'River Channel Changes'), ('other', 'Other')], default='rainfall', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Glof',
            fields=[
                ('glof_key', models.AutoField(primary_key=True, serialize=False)),
                ('water_level', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('casualties', models.IntegerField(blank=True, null=True)),
                ('cause', models.CharField(choices=[('avalanche', 'Avalanche'), ('earthquake', 'Earthquake'), ('dam_failure', 'Dam Failure'), ('other', 'Other')], default='avalanche', max_length=100)),
                ('loss', models.IntegerField(blank=True, null=True)),
                ('latitude_epicenter', models.FloatField(blank=True, null=True)),
                ('longitude_epicenter', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Landslide',
            fields=[
                ('landslide_key', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('casualties', models.IntegerField(blank=True, null=True)),
                ('loss', models.IntegerField(blank=True, null=True)),
                ('cause', models.CharField(choices=[('earthquake', 'Earthquake'), ('rainfall', 'Rainfall'), ('soil_erosion', 'Soil Erosion'), ('other', 'Other')], default='rainfall', max_length=100)),
                ('latitude_epicenter', models.FloatField(blank=True, null=True)),
                ('longitude_epicenter', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='static/profiles/')),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
