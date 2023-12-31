# Generated by Django 4.2.6 on 2023-11-02 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_doctor_describe_alter_doctor_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='id_schedule_doctor',
            new_name='schedule_doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='id_hospital',
            new_name='hospital',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='id_specialty',
            new_name='specialty',
        ),
        migrations.RenameField(
            model_name='scheduler_doctor',
            old_name='id_doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='scheduler_doctor',
            old_name='id_schedule',
            new_name='schedule',
        ),
        migrations.RenameField(
            model_name='servicedoctor',
            old_name='id_doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='servicedoctor',
            old_name='id_service',
            new_name='service',
        ),
    ]
