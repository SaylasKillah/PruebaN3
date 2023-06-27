from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm,RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def galeria(request):
    producto = Producto.objects.all()
    datos={
        'producto': producto
    }
    return render(request,'galeria.html',datos)

@login_required
def almacen(request):
    producto=Producto.objects.all()    #obtenemos todos los obj de la clase Producto
    datos={'prod' : producto}     #creamos diccionario que recibe la colección de objetos
    return render(request, 'almacen.html', datos)   #enviamos parámetro al almacen

@login_required
def crear(request):
    if request.method=='POST':
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect('almacen')
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html',{'productoform': productoform})

@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(idproducto=id)  #obtenemos un objeto por su pk
    productoEliminado.delete()
    return redirect('almacen')

@login_required
def modificar(request,id):
    producto = Producto.objects.get(idproducto=id)         #obtenemos un objeto por su pk
    datos ={
        'form':ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect ('almacen')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data = {
        'form' : RegistroUserForm()         #creamos un objeto de tipo forms para user
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('Amigosfieles')
        data["form"] = formulario
    return render(request, 'registration/registrar.html', data)

def login(request):
    return render(request, 'login.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def formulario(request):
    return render(request, 'formulario.html')

def info(request):
    return render(request, 'info.html')

def ubicanos(request):
    return render(request, 'ubicanos.html')

def contactanos(request):
    return render(request, 'contactanos.html')