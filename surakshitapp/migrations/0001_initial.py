# Generated by Django 4.2.5 on 2023-12-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('speed', models.PositiveIntegerField()),
            ],
        ),
    ]
