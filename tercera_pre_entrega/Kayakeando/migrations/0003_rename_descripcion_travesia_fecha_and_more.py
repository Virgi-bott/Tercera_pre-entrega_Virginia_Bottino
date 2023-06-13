# Generated by Django 4.2.1 on 2023-06-13 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kayakeando', '0002_rename_localidad_club_ciudad_remove_club_provincia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travesia',
            old_name='descripcion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='travesia',
            old_name='ubicacion',
            new_name='partida',
        ),
        migrations.AddField(
            model_name='travesia',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
