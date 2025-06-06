# Generated by Django 5.2 on 2025-05-24 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_remove_paralelo_capacidad_maxima'),
        ('institucion', '0003_modulo_pisos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='curso',
        ),
        migrations.AddField(
            model_name='clase',
            name='materia_curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clases', to='academico.materiacurso', verbose_name='Materia en Curso'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clases', to='institucion.aula', verbose_name='Aula asignada'),
        ),
    ]
