import django
from django.forms import ModelForm
from django import forms
from django.db.models import fields
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'lastname', 'idCode', 'phone', 'position')
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'idCode': 'Codigo Personal',
            'phone': 'Teléfono Celular',
            'position': 'Posición'
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Seleccione'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']
