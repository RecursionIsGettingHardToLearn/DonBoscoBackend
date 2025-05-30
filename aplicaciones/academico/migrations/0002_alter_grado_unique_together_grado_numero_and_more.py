# Generated by Django 5.2 on 2025-05-22 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
        ('institucion', '0002_colegio_super_admin_fk_modulo_colegio_fk_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grado',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='grado',
            name='numero',
            field=models.PositiveSmallIntegerField(default=1, help_text='Número de grado dentro del nivel (1 a 6)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterUniqueTogether(
            name='grado',
            unique_together={('unidad_educativa', 'nivel_educativo', 'numero')},
        ),
    ]
