# Generated by Django 4.2.5 on 2023-10-03 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_account_id_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='app.account'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='app.account'),
        ),
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.account'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.BooleanField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='app.account')),
            ],
        ),
    ]
