# Generated by Django 4.2.6 on 2023-11-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_specialty_icon_tool_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
