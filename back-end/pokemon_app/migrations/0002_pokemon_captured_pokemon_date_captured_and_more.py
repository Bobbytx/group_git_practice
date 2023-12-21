# Generated by Django 4.2.4 on 2023-08-22 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='captured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='date_captured',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='date_encountered',
            field=models.DateField(default='2008-01-01'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]