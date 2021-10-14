from django.contrib.auth.forms import UsernameField
from django.db import models
from django.db.models.manager import ManagerDescriptor


# Create your models here.
#Modelo de datos (BD)

class Position (models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    idCode= models.CharField(max_length=5)
    phone= models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


    