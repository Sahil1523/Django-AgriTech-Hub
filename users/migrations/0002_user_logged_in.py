# Generated by Django 4.0.6 on 2022-07-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
    ]