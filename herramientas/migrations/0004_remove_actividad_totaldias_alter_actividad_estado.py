# Generated by Django 4.1.7 on 2023-07-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0003_alter_nombramiento_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='totalDias',
        ),
        migrations.AlterField(
            model_name='actividad',
            name='estado',
            field=models.CharField(choices=[('EN_PROCESO', 'En proceso'), ('FINAIZADA', 'Finalizada')], max_length=50, verbose_name='Estado Actual PT'),
        ),
    ]
