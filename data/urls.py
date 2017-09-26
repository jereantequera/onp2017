#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from views import EstablecimientoView, TemperaturaView, AguaView, LuzView, LogsView, DeleteAguaView, DeleteLuzView, DeleteTemperatureView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'establecimientos', EstablecimientoView)
router.register(r'temperatura', TemperaturaView)
router.register(r'agua', AguaView)
router.register(r'luz', LuzView)
router.register(r'logs', LogsView)
router.register(r'deleteAgua', DeleteAguaView, base_name="deleteAgua")
router.register(r'deleteLuz', DeleteLuzView, base_name="deleteLuz")
router.register(r'deleteTemperature', DeleteTemperatureView, base_name="deleteTemperature")
urlpatterns = [
               url(r'^api/', include(router.urls, namespace='api')),
               ]