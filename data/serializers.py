from django.contrib.auth.models import User, Group
from .models import Establecimiento, Temperatura, Agua, Luz, Logs
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class EstablecimientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Establecimiento
        fields = ('id_criadero', 'denominacion', 'empresa', 'clave', 'direccion')
        extra_kwargs = {
            'url': {'view_name': 'establecimiento-detail', 'lookup_field': 'url'},
        }

    def create(self, validated_data):
        Logs(accion="creando establecimiento").save()
        return Establecimiento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Logs(accion="updating establecimiento").save()
        instance.denominacion = validated_data.get('denominacion', instance.denominacion)
        instance.empresa = validated_data.get('empresa', instance.empresa)
        instance.clave = validated_data.get('clave', instance.clave)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        return instance


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    id_criadero = EstablecimientoSerializer()

    class Meta:
        model = Temperatura
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'temperatura-detail', 'lookup_field': 'url'},
        }

    def create(self, validated_data):
        print validated_data
        Logs(accion="creando temperatura").save()
        return Temperatura.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Logs("update temperatura").save()
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.unidad = validated_data.get('unidad', instance.unidad)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.id_criadero = validated_data.get('id_criadero', instance.id_criadero)
        return instance


class AguaSerializer(serializers.HyperlinkedModelSerializer):
    id_criadero = EstablecimientoSerializer()

    class Meta:
        model = Agua
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'agua-detail', 'lookup_field': 'url'},
        }

    def create(self, validated_data):
        Logs(accion="creando agua").save()
        return Agua.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Logs("update agua").save()
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.unidad = validated_data.get('unidad', instance.unidad)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.id_criadero = validated_data.get('id_criadero', instance.id_criadero)
        return instance


class LuzSerializer(serializers.HyperlinkedModelSerializer):
    id_criadero = EstablecimientoSerializer()

    class Meta:
        model = Luz
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'agua-detail', 'lookup_field': 'url'},
        }

    def create(self, validated_data):
        Logs(accion="creando luz").save()
        return Luz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Logs("update luz").save()
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.unidad = validated_data.get('unidad', instance.unidad)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.id_criadero = validated_data.get('id_criadero', instance.id_criadero)
        return instance


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'logs-detail', 'lookup_field': 'url'},
        }
