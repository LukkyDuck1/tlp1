# Generated by Django 5.0.6 on 2024-06-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_estudiante_contraseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='descripcion',
            field=models.CharField(max_length=255, verbose_name='Descripcion'),
        ),
    ]