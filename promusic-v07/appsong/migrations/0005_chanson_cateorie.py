# Generated by Django 2.1.7 on 2019-03-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsong', '0004_auto_20190316_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanson',
            name='cateorie',
            field=models.ManyToManyField(to='appsong.Categorie'),
        ),
    ]
