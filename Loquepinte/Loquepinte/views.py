from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
from django.shortcuts import render , redirect # ademas del render coloco el redirect para redireccionar
#from django.contrib.auth.decorators import login_required # este sirve para obligar que este logeado para ingresar
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, "index.html")

def principal(request):
    return render(request, "principal.html")

def restaurante(request):
    return render(request, "restaurante.html")

def contactar(request):
    if request.method == 'POST':
        nombre = request.POST["txtNombre"]

        llamar = request.POST.get('txt_llamar', False)

        numero_llamen= 'Quieren que lo llamen: ' + str(llamar)

        Datos='Nombre del Restaurante: '+ request.POST["txtNombre"] +'\nCorreo: '+ request.POST["txtEmail"] + ' \nTelefono:' + request.POST["txtNumero"] + ' \nDireccion:' + request.POST["txtDomicilio"] + ' \nComentario:\n' + request.POST["txtComentario"] + '\n' + numero_llamen        
        

        email_desde=settings.EMAIL_HOST_USER
        email_para=["informatorio2020@gmail.com"]
        send_mail(nombre,Datos,email_desde,email_para,fail_silently=False)
        return render(request, "C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/contacto_exitoso.html")

    return render(request, "C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/principal.html")

def registro_usuario(request):
    data= {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid(): # con esto pregunto si el formulario es valido
            formulario.save()
            # Ahora lo que hago es si es correcto lo redirijo voy a importar arriba login ,authenticate
            username = formulario.cleaned_data['username'] # con .cleaned_data lo que hago es obtener los valores
            password= formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password) # con esto se autenfica ahora se hace el login
            login(request,user)
            return render(request, "principal.html")
        else:
            return render(request, "registration/error_registro.html")
    return render(request, 'registration/registrar.html', data)

def error(request):
    return render(request, "registration/error_registro.html")


