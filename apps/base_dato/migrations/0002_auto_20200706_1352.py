# Generated by Django 3.0.7 on 2020-07-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_dato', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viaje',
            name='numero_unidad',
        ),
        migrations.AddField(
            model_name='viaje',
            name='numero_unidad',
            field=models.ManyToManyField(to='base_dato.unidade', verbose_name='Número de la unidad'),
        ),
    ]
