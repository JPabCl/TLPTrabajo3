# Generated by Django 5.0.4 on 2024-07-07 16:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('nombrePlanta', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('nombreProducto', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litros_producidos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_produccion', models.DateField()),
                ('turno', models.CharField(choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], max_length=2)),
                ('hora_registro', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('anulado', models.BooleanField(default=False)),
                ('fecha_anulacion', models.DateTimeField(blank=True, null=True)),
                ('anulado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anulaciones', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modificaciones', to=settings.AUTH_USER_MODEL)),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.planta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.producto')),
            ],
        ),
    ]
