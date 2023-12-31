# Generated by Django 4.1.7 on 2023-10-02 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_account_remove_user_email_remove_user_id_userinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('id_specialty', models.IntegerField()),
                ('id_hospital', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('gender', models.BooleanField()),
                ('years_of_experience', models.IntegerField()),
                ('descripe', models.TextField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('formula', models.CharField(max_length=255)),
                ('questions', models.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='id_role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(default='user', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='ServiceDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(max_length=7)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('id_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('id_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
