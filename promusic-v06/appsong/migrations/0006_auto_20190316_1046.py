# Generated by Django 2.1.7 on 2019-03-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsong', '0005_chanson_cateorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chanson',
            old_name='cateorie',
            new_name='categorie',
        ),
    ]