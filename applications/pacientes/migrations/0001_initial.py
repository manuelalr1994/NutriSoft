# Generated by Django 4.0 on 2022-04-23 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('escolaridad', models.CharField(max_length=10)),
                ('tipo_sangre', models.CharField(max_length=3)),
                ('estado_civil', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]