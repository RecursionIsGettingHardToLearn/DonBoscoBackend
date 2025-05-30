# Generated by Django 5.2 on 2025-04-27 00:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('ASI', 'Asistió'), ('FAL', 'Faltó'), ('TAR', 'Tardanza'), ('JUS', 'Falta justificada')], max_length=3)),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Asistencia General',
                'verbose_name_plural': 'Asistencias Generales',
                'db_table': 'asistencia_general',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Comportamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('POS', 'Positivo'), ('NEG', 'Negativo'), ('OBS', 'Observación')], max_length=3)),
                ('gravedad', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Registro de Comportamiento',
                'verbose_name_plural': 'Registros de Comportamiento',
                'db_table': 'comportamiento',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('motivo', models.TextField()),
                ('estado', models.CharField(choices=[('SOL', 'Solicitada'), ('APR', 'Aprobada'), ('REC', 'Rechazada'), ('FIN', 'Finalizada')], default='SOL', max_length=3)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='licencias/')),
            ],
            options={
                'verbose_name': 'Licencia',
                'verbose_name_plural': 'Licencias',
                'db_table': 'licencia',
                'ordering': ['-fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='AsistenciaClase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.CharField(choices=[('ASI', 'Presente'), ('FAL', 'Ausente'), ('TAR', 'Tardanza'), ('LIC', 'Con licencia')], max_length=3)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='academico.clase')),
            ],
            options={
                'verbose_name': 'Asistencia por Clase',
                'verbose_name_plural': 'Asistencias por Clases',
                'db_table': 'asistencia_clase',
                'ordering': ['-fecha', 'hora'],
            },
        ),
    ]
