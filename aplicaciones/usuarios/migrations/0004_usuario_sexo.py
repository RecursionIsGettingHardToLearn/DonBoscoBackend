# Generated by Django 5.2 on 2025-05-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_bitacora_options_alter_superadmin_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1),
        ),
    ]
