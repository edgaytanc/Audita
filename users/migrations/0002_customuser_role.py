# Generated by Django 4.1.7 on 2023-10-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('auditor', 'Auditor'), ('supervisor', 'Supervisor'), ('jefe_auditoria', 'Jefe de Auditoria')], default='auditor', max_length=20),
        ),
    ]
