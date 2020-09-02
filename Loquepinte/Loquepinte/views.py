from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def principal(request):
    return render(request, "principal.html")

def restaurante(request):
    return render(request, "restaurante.html")

def contactar(request):
    if request.method == 'POST':
        nombre = request.POST["txtNombre"]
        Datos='Nombre del Restaurante: '+ request.POST["txtNombre"] +'\nCorreo: '+ request.POST["txtEmail"] + ' \nTelefono:' + request.POST["txtNumero"] + ' \nDireccion:' + request.POST["txtDomicilio"] + '\nQuiere que lo llame:' + request.POST["txt_llamar"] + ' \nComentario:\n' + request.POST["txtComentario"]
        email_desde=settings.EMAIL_HOST_USER
        email_para=["informatorio2020@gmail.com"]
        send_mail(nombre,Datos,email_desde,email_para,fail_silently=False)
        return render(request, "C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/contacto_exitoso.html")

    return render(request, "C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/principal.html")


