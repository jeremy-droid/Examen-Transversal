from django.urls import path, include
from .views import home, productos, quienesSomos, contacto, sismos, registro, form_proveedor, form_mod_proveedor, form_del_proveedor

urlpatterns = [
    path('', home, name="home"),
    path('productos', productos, name="productos"),
    path('quienesSomos', quienesSomos, name="quienesSomos"),
    path('contacto', contacto, name="contacto"),
    path('sismos', sismos, name="sismos"),
    path('registro', registro, name="registro"),
    path('form_proveedor', form_proveedor, name="form_proveedor"),
    path('form_mod_proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form_del_proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
    
    path('api/',include('rest_proveedor.urls')),
]