# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Establecimiento (models.Model):
    id_criadero = models.AutoField(primary_key=True)
    denominacion = models.CharField("Denominacion comercial del Criadero Avícola", max_length=255, null=False)
    empresa = models.CharField("Empresa propietaria del establecimiento", max_length=255, null=False)
    clave = models.CharField("Clave Fiscal", max_length=255, null=False)
    direccion = models.CharField("Direccion", max_length=255, null=False)


class Temperatura (models.Model):
    id_temp = models.AutoField(primary_key=True)
    fecha = models.DateField("fecha")
    hora = models.TimeField("hora")
    valor = models.FloatField("valor")
    unidad = models.CharField("unidad fisica", max_length=1)
    estado = models.CharField("estado del transductor", max_length=24)
    id_criadero = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)


class Agua (models.Model):
    id_agua = models.AutoField(primary_key=True)
    fecha = models.DateField("fecha")
    hora = models.TimeField("hora")
    valor = models.FloatField("valor")
    unidad = models.CharField("unidad fisica", max_length=3)
    estado = models.CharField("estado del transductor", max_length=24)
    id_criadero = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)


class Luz (models.Model):
    id_luz = models.AutoField(primary_key=True)
    fecha = models.DateField("fecha")
    hora = models.TimeField("hora")
    valor = models.FloatField("valor")
    unidad = models.CharField("unidad fisica", max_length=3)
    estado = models.CharField("estado del transductor", max_length=24)
    id_criadero = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)


class Logs(models.Model):
    id_logs = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)

