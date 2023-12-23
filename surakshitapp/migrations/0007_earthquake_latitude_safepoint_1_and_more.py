# Generated by Django 5.0 on 2023-12-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshitapp', '0006_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='earthquake',
            name='latitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='latitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='latitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='latitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='latitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='longitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='longitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='longitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='longitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='longitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='latitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='latitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='latitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='latitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='latitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='longitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='longitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='longitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='longitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flood',
            name='longitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='latitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='latitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='latitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='latitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='latitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='longitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='longitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='longitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='longitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glof',
            name='longitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='latitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='latitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='latitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='latitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='latitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='longitude_safepoint_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='longitude_safepoint_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='longitude_safepoint_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='longitude_safepoint_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landslide',
            name='longitude_safepoint_5',
            field=models.FloatField(blank=True, null=True),
        ),
    ]