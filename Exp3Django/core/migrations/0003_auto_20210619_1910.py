# Generated by Django 3.2.3 on 2021-06-19 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_registro_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='contraseña',
            field=models.CharField(max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='usuario',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Usuario'),
        ),
    ]
