# Generated by Django 5.1.4 on 2025-02-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0002_alter_emprunt_date_emprunt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='rendu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='media',
            name='quantite_disponible',
            field=models.IntegerField(default=1),
        ),
    ]
