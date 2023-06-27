from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idproducto', 'producto', 'precio', 'imagen']
        labels = {
            'idproducto': 'Idproducto',
            'producto': 'Producto',
            'precio': 'Precio',
            'imagen': 'Imagen'
        }
        widgets = {
            'idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese idproducto..',
                    'id': 'idproducto',
                }
            ),
            'producto':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese producto..',
                    'id': 'producto',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio..',
                    'id': 'precio',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            )
        }