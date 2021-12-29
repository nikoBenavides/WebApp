import django
from django.forms import ModelForm
from django import forms
from django.db.models import fields
from .models import Activity, Person
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


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('activity_name', 'activity_description', 'activity_date_created','activity_date_end','person',
                    'urgency', 'hours','status')
        labels = {
            'activity_name': 'Nombre Actividad',
            'activity_description': 'Descripción',
            'activity_date_created': 'Fecha de Inicio:',
            'activity_date_end':'Fecha Fin:',
            'hours':'Horas estimadas:',
            'status':'Estado',
            'person':'Empleado asigando:',
            'urgency': 'Urgencia:'            
        }

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['urgency'].empty_label = 'Seleccione'
        self.fields['person'].empty_label = 'Seleccione'
        self.fields['status'].empty_label = 'Seleccione'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']

