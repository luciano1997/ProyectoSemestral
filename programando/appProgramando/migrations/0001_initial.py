# Generated by Django 2.2.6 on 2019-10-14 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=70)),
                ('rut', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=65)),
                ('telefono', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=70)),
                ('comuna', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('tipo_vivienda', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matricula', models.DateField()),
                ('activo', models.BooleanField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProgramando.Curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProgramando.Usuario')),
            ],
        ),
    ]
