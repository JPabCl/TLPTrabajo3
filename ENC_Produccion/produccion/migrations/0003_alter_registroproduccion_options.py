# Generated by Django 5.0.4 on 2024-07-07 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_remove_planta_ubicacion_remove_producto_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registroproduccion',
            options={'permissions': [('can_toggle_anulado', 'Can toggle anulado field')]},
        ),
    ]