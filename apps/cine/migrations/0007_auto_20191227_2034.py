# Generated by Django 2.2.6 on 2019-12-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0006_auto_20191227_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcion',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Cancelada', 'Cancelada')], default='Disponible', max_length=200),
        ),
    ]
