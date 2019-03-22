# Generated by Django 2.1.7 on 2019-03-16 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=30)),
                ('classe', models.CharField(blank=True, max_length=20)),
                ('couleur', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chanson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.CharField(blank=True, max_length=50)),
                ('titre', models.CharField(blank=True, max_length=50)),
                ('fichier', models.CharField(blank=True, max_length=200)),
                ('youtube', models.URLField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
