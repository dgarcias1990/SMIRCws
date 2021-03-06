# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class InicioLocalization(models.Model):
    usuario = models.ForeignKey('InicioUserapp')
    latitud = models.FloatField()
    longitud = models.FloatField()
    altitud = models.FloatField()
    charla = models.BooleanField()
    fechahora = models.DateTimeField(db_column='fechaHora', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inicio_localization'


class InicioUserapp(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=254)
    contrasena = models.CharField(max_length=20)
    fechaalta = models.DateTimeField(db_column='fechaAlta', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True)  # Field name made lowercase.
    sesionactiva = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'inicio_userapp'
