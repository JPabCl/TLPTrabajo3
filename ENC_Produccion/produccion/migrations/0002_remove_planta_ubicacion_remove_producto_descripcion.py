# Generated by Django 5.0.4 on 2024-07-07 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='ubicacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
    ]