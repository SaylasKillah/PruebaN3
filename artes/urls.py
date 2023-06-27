from django.urls import path
from .views import index,galeria,almacen,crear,eliminar,modificar,info,registrarse,ubicanos,contactanos,formulario,login,registrar

urlpatterns=[ 
    path('', index, name="index"),
    path('galeria/',galeria, name="galeria"),
    path('almacen/',almacen, name="almacen"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('info/',info, name="info"),
    path('registrar/',registrar, name="registrar"),
    path('login/',login, name="login"),
    path('registrarse/',registrarse, name="registrarse"),
    path('ubicanos/',ubicanos, name="ubicanos"),
    path('contactanos/', contactanos, name="contactanos"),
    path('formulario/', formulario, name="formulario"),
]