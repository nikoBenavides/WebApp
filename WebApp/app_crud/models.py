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
    points=models.CharField(max_length=50)
    if status == 'To Do':
        points = 0
    else:
        if status == 'In Progress':
            points = 0.5
        else:
            if status == 'Blocked':
                points = 0.5
            else:
                if status == 'Testing':
                    points = 2
                else:
                    if status == 'Blocked':
                        points = 1.5
                    else:
                        points = 3
        

    def __str__(self):
        return self.status



        
class Urgency (models.Model):
    points=models.CharField(max_length=50)
    urgency=models.CharField(max_length=50)
    
    if urgency == 'Baja':
        points = 1
    else:
        if urgency == 'Media':
            points = 2
        else:
            points =3

    def __str__(self):
        return self.urgency
    
    
            
    


class Person(models.Model):
    name = models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    idCode= models.CharField(max_length=5)
    phone= models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

def SumPoints( sum ):
    sum =  Status.__getpoints__ + Urgency.__getpoints__
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
    points=models.FloatField(sum, null=True)
    
    
                        






    
   
    