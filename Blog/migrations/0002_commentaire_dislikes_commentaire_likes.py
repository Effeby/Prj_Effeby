# Generated by Django 4.1.5 on 2023-01-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
