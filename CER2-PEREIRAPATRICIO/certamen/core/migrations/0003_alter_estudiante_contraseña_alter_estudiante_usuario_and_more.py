# Generated by Django 5.0.6 on 2024-06-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_estudiante_contraseña_estudiante_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='contraseña',
            field=models.CharField(max_length=80, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='usuario',
            field=models.CharField(max_length=80, verbose_name='Nombre de Uusario'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='contraseña',
            field=models.CharField(max_length=80, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='usuario',
            field=models.CharField(max_length=80, verbose_name='Nombre de Uusario'),
        ),
    ]
