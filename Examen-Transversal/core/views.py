from core.forms import ProveedorForm
from .models import Proveedor
from django.http import request
from django.shortcuts import redirect, render
from core.models import Proveedor

def home(request):
 return render(request, 'core/home.html')

def productos(request):
  return render(request,'core/nuestrosproductos.html')

def quienesSomos(request):
  return render(request,'core/quienesSomos.html')

def contacto(request):
  return render(request, 'core/contacto.html')

def sismos(request):
  return render(request, 'core/sismos.html')

##############################################################

def registro(request):
    proveedor = Proveedor.objects.all()
    datos = {
      "proveedores" : proveedor
    }
    return render(request, 'core/registro.html', datos)

##############################################################
def form_proveedor(request):

  datos = {
    'form' : ProveedorForm()
  }

  if request.method == 'POST':
    formulario = ProveedorForm(request.POST)
    if formulario.is_valid:
      formulario.save()
      datos['mensaje'] = "Datos guardados correctamente"

  return render(request, 'core/form_proveedor.html', datos)
##############################################################


def form_mod_proveedor(request, id):
  
  proveedor = Proveedor.objects.get(identificacion=id)

  datos = {
    'form' : ProveedorForm(instance=proveedor)
  }

  if request.method == 'POST':
    formulario = ProveedorForm(request.POST, instance=proveedor)
    if formulario.is_valid:
      formulario.save()
      datos['mensaje'] = "Se modificó exitosamente"
  return render(request, 'core/form_mod_proveedor.html', datos)

##############################################################

def form_del_proveedor(request, id):

  proveedor = Proveedor.objects.get(identificacion=id)
  proveedor.delete()
  
  return redirect(to="registro")