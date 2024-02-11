from django.contrib.auth.models import Group, User
from rest_framework import serializers
from alquiler_patinetes.models import Usuario, Patinete, Alquiler


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['url', 'numero', 'tipo', 'precio_desbloqueo', 'precio_minuto']


class AlquilerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alquiler
        fields = ['url', 'usuario', 'patinete', 'fecha_desbloqueo', 'fecha_entrega', 'coste_final']


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'user', 'debito']

