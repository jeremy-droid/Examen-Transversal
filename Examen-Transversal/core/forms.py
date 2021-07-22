from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):

    class Meta:
        model = Proveedor
        fields = ['identificacion','nombre','telefono','direccion','email','contraseña','moneda','pais']