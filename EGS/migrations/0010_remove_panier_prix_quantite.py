# Generated by Django 4.1.5 on 2023-02-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EGS', '0009_remove_panier_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='prix_quantite',
        ),
    ]
