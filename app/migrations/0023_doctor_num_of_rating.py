# Generated by Django 4.2.6 on 2023-11-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_appointment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='num_of_rating',
            field=models.IntegerField(default=0),
        ),
    ]