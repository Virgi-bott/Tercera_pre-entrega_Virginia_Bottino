# Generated by Django 4.2.1 on 2023-06-12 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kayakeando', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='localidad',
            new_name='ciudad',
        ),
        migrations.RemoveField(
            model_name='club',
            name='provincia',
        ),
    ]
