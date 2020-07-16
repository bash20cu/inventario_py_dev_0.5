# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-30 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicio_id', models.AutoField(primary_key=True, serialize=False)),
                ('servicio', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('comentario', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]