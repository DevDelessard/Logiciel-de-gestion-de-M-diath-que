# Generated by Django 5.1.4 on 2025-02-12 10:08

import bibliotheque.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('livre', 'Livre'), ('dvd', 'DVD'), ('cd', 'CD'), ('jeu', 'Jeu de plateau')], max_length=10)),
                ('disponible', models.BooleanField(default=True)),
                ('empruntable', models.BooleanField(default=True)),
                ('auteur', models.CharField(blank=True, max_length=255, null=True)),
                ('realisateur', models.CharField(blank=True, max_length=255, null=True)),
                ('artiste', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_inscription', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(default=django.utils.timezone.now)),
                ('date_retour_prevu', models.DateField(default=bibliotheque.models.default_date_retour)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.media')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.membre')),
            ],
        ),
    ]
