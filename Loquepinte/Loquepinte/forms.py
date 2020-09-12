from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm # esto son los formularios que nos da django
from django.contrib.auth.models import User
from modulos.Comentarios.models import Restaurant , Comment
class CustomUserForm(UserCreationForm):
     class Meta :
          model = User
          fields =['first_name', 'last_name','email','username', 'password1', 'password2']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)