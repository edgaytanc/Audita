# Generated by Django 4.1.7 on 2023-10-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancegeneral',
            name='archivo_actual',
            field=models.FileField(upload_to='balance_actual', verbose_name='Balance o Estado de Resultados Actual'),
        ),
        migrations.AlterField(
            model_name='balancegeneral',
            name='archivo_anterior',
            field=models.FileField(upload_to='balance_anterior/', verbose_name='Balance o Estado de Resultados Anterior'),
        ),
    ]
