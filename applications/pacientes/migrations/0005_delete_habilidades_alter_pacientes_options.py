# Generated by Django 5.0.3 on 2024-03-15 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_delete_pacientess'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Habilidades',
        ),
        migrations.AlterModelOptions(
            name='pacientes',
            options={'ordering': ['codigo'], 'verbose_name': 'Mis Pacientes', 'verbose_name_plural': 'Lista de Pacientes'},
        ),
    ]