# Generated by Django 4.1.2 on 2023-02-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlantSitterApp', '0011_alter_publication_idaccepteur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conseil',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]