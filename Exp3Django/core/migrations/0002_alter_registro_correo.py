# Generated by Django 3.2.3 on 2021-06-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='correo',
            field=models.CharField(max_length=100, verbose_name='Correo Electronico'),
        ),
    ]