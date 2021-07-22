from rest_framework import serializers
from core.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['identificacion','nombre','telefono','direccion','email','contraseña','moneda','pais']
