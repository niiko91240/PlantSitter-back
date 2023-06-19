# Generated by Django 4.1.2 on 2023-02-03 10:35

import PlantSitterApp.modeles.publication
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numVoie', models.IntegerField()),
                ('rue', models.CharField(max_length=40)),
                ('codePostal', models.IntegerField()),
                ('ville', models.CharField(max_length=40)),
                ('complement', models.CharField(blank=True, max_length=40, null=True)),
                ('coordonneeX', models.FloatField(max_length=5)),
                ('coordonneeY', models.FloatField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Plante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('nomScientifique', models.CharField(max_length=60)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('mdp', models.CharField(max_length=30)),
                ('isBotaniste', models.BooleanField()),
                ('idAdresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse', to='PlantSitterApp.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('heureDebut', models.TimeField(blank=True, null=True)),
                ('heureFin', models.TimeField(blank=True, null=True)),
                ('titre', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=PlantSitterApp.modeles.publication.upload_to)),
                ('idAccepteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepteur', to='PlantSitterApp.utilisateur')),
                ('idCreateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createur', to='PlantSitterApp.utilisateur')),
                ('plante', models.ManyToManyField(related_name='plantes', to='PlantSitterApp.plante')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('heure', models.TimeField(blank=True, null=True)),
                ('image', models.FileField(upload_to='')),
                ('idPublication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='PlantSitterApp.publication')),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilisateur', to='PlantSitterApp.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Conseil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('idPlante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plante', to='PlantSitterApp.plante')),
            ],
        ),
    ]
