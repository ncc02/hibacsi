# Generated by Django 4.2.6 on 2023-11-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
