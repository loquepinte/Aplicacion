from django.db import models
# Create your models here.
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm # esto son los formularios que nos da django
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
     class Meta :
          model = User
          fields =['first_name', 'last_name','email','username', 'password1', 'password2']


class Restaurant(models.Model):
    Id= models.AutoField(primary_key=True)
    Nombre= models.CharField(max_length=400)
    Direccion= models.CharField(max_length=200)
    Telefono= models.IntegerField()
# EL METODO RELATED_NAME NOS PERMITE ACCEDER AL ODELO CON EL METODO POST
class Comment(models.Model):
    Id=models.CharField(max_length=5, primary_key=True)
    Id_Restaurant = models.ForeignKey(Restaurant, related_name='comments',null=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    

class Comentario(models.Model):
    usuario=models.CharField(max_length=50)
    Nombre_restaurant=models.CharField(max_length=100)
    mensaje=models.TextField()