# Generated by Django 4.1.7 on 2023-04-19 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herramientas', '0006_alter_actividad_abril_alter_actividad_agosto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nombramiento',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nombramiento',
            name='nombramiento',
            field=models.CharField(max_length=10, unique=True, verbose_name='Nombramiento'),
        ),
    ]
