from django.contrib.auth.forms import UsernameField
from django.db import models
from django.db.models.fields import BigIntegerField
from django.db.models.manager import ManagerDescriptor
from datetime import date


# Create your models here.
#Modelo de datos (BD)

class Position (models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Status (models.Model):
    status=models.CharField(max_length=100)
    points_sts=models.CharField(max_length=50)
    def __str__(self):
        return self.status

class Urgency (models.Model):
    points_urg=models.CharField(max_length=50)
    urgency=models.CharField(max_length=50)

    def __str__(self):
        return self.urgency
 
class Person(models.Model):
    name = models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    person_points = models.IntegerField(default=0)
    person_bonus = models.BooleanField(default=False)    
    def __str__(self):
        return self.name

# persons = Person.objects.all()
# print(persons)

def SumPoints( sum ):
    sum =  Status.__getattribute__('points_sts') + Urgency.__getattribute__('points_urg')
    return sum

class Activity(models.Model):

    activity_name = models.CharField(max_length=500, null=True)
    activity_description = models.CharField(max_length=1000, null=True)
    activity_date_created = models.DateField(default=date.today, null=True)
    activity_date_end = models.DateField(default=date.today, null=True)
    hours = models.CharField(max_length=2, null=True)
    status=models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    person=models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    urgency=models.ForeignKey(Urgency, null=True,on_delete=models.SET_NULL)
    points=models.FloatField(default=0)
    
    
    
                        






    
   
    