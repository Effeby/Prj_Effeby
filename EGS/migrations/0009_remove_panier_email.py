# Generated by Django 4.1.5 on 2023-02-07 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EGS', '0008_panier_prix_quantite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='email',
        ),
    ]
