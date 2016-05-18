# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InicioLocalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('altitud', models.FloatField()),
                ('charla', models.IntegerField()),
                ('fechahora', models.DateTimeField(db_column='fechaHora')),
            ],
            options={
                'db_table': 'inicio_localization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InicioUserapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('fechanacimiento', models.DateField(db_column='fechaNacimiento')),
                ('email', models.CharField(unique=True, max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
                ('fechaalta', models.DateTimeField(db_column='fechaAlta')),
                ('lastlogin', models.DateTimeField(db_column='lastLogin')),
            ],
            options={
                'db_table': 'inicio_userapp',
                'managed': False,
            },
        ),
    ]
