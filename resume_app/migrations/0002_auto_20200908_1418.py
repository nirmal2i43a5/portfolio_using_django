# Generated by Django 2.0 on 2020-09-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='semester',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
