# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import viewsets
from data.serializers import UserSerializer, \
    EstablecimientoSerializer, \
    TemperatureSerializer,\
    AguaSerializer, \
    LuzSerializer, \
    LogsSerializer
from .models import Establecimiento, Agua, Temperatura, Luz, Logs


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class EstablecimientoView(viewsets.ModelViewSet):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializer


class TemperaturaView(viewsets.ModelViewSet):
    queryset = Temperatura.objects.all()
    serializer_class = TemperatureSerializer


class AguaView(viewsets.ModelViewSet):
    queryset = Agua.objects.all()
    serializer_class = AguaSerializer


class LuzView(viewsets.ModelViewSet):
    queryset = Luz.objects.all()
    serializer_class = LuzSerializer


class LogsView(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
