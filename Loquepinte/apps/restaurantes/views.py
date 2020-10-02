from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404 # ademas del render coloco el redirect para redireccionar
from django.contrib.auth.decorators import login_required # este sirve para obligar que este logeado para ingresar
from django.contrib.auth import login, authenticate
from django.db.models import Avg

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def principal(request):
    prom1 = Comentario.objects.aggregate(Avg('valoracion'))
    try:
        promedio1 = int(prom1['valoracion__avg'])
    except:
        promedio1 = 1

    prom2 = ComentarioSurtidor.objects.aggregate(Avg('valoracion'))
    try:
        promedio2 = int(prom2['valoracion__avg'])
    except:
        promedio2 = 1 

    prom3 = ComentarioLomo.objects.aggregate(Avg('valoracion'))
    try:
        promedio3 = int(prom3['valoracion__avg'])
    except:
        promedio3 = 1

    prom4 = ComentarioChimenea.objects.aggregate(Avg('valoracion'))
    try:
        promedio4 = int(prom4['valoracion__avg'])
    except:
        promedio4 = 1  

    prom5 = ComentarioNanas.objects.aggregate(Avg('valoracion'))
    try:
        promedio5 = int(prom5['valoracion__avg'])
    except:
        promedio5 = 1  

    prom6 = ComentarioJose.objects.aggregate(Avg('valoracion'))
    try:
        promedio6 = int(prom6['valoracion__avg'])
    except:
        promedio6 = 1

    contexto={'promedio1':promedio1,'promedio2':promedio2,'promedio3':promedio3,'promedio4':promedio4,'promedio5':promedio5,'promedio6':promedio6,}  

    return render(request, "restaurantes/principal.html",contexto)

def restaurante(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''

    # Para mostrar los comentarios:
    Ultimoscomentarios = Comentario.objects.all().order_by('-id')[:3]
    comentarios = Comentario.objects.all().order_by('-id')
    prom = Comentario.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    } 

    # para el comentario del usuario:
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_Usuario"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=1)
        texto=request.POST["txt_Comentario"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        
        comentario = Comentario(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../restaurante/")
    return render(request, "restaurantes/restaurante.html", contexto)

def el_surtidor(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioSurtidor.objects.all().order_by('-id')[:3]
    comentarios = ComentarioSurtidor.objects.all().order_by('-id')
    prom = ComentarioSurtidor.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    } 
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioSur"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=2)
        texto=request.POST["txt_ComentarioSur"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioSurtidor(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../el_surtidor/")
    return render(request, "restaurantes/el_surtidor.html", contexto)

def el_patron(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioLomo.objects.all().order_by('-id')[:3]
    comentarios = ComentarioLomo.objects.all().order_by('-id')
    prom = ComentarioLomo.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    } 
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioLomo"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=3)
        texto=request.POST["txt_ComentarioLomo"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioLomo(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../el_patron/") 
    return render(request, "restaurantes/el_patron.html", contexto)

def la_chimenea(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioChimenea.objects.all().order_by('-id')[:3]
    comentarios = ComentarioChimenea.objects.all().order_by('-id')
    prom = ComentarioChimenea.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    } 
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioChi"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=4)
        texto=request.POST["txt_ComentarioChi"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioChimenea(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../la_chimenea/") 
    return render(request, "restaurantes/la_chimenea.html", contexto)

def nanas(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioNanas.objects.all().order_by('-id')[:3]
    comentarios = ComentarioNanas.objects.all().order_by('-id')
    prom = ComentarioNanas.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    } 
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioNanas"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=5)
        texto=request.POST["txt_ComentarioNanas"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioNanas(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../nanas/")
    return render(request, "restaurantes/nanas.html", contexto)
    
def san_jose(request):
    '''Esta función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioJose.objects.all().order_by('-id')[:3]
    comentarios = ComentarioJose.objects.all().order_by('-id')
    prom = ComentarioJose.objects.aggregate(Avg('valoracion'))
    try:
        promDecimal = str(prom['valoracion__avg'])
        promedio = int(prom['valoracion__avg'])
    except:
        promDecimal = "1.0"
        promedio = 1
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios, 'promedio':promedio, 'promDecimal':promDecimal[:3],
    }
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioJo"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=6)
        texto=request.POST["txt_ComentarioJo"]
        calificacion = "1"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioJose(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../san_jose/") 
    return render(request, "restaurantes/san_jose.html", contexto)

def contactar(request):
    if request.method == 'POST':
        nombre = request.POST["txtNombre"]

        llamar = request.POST.get('txt_llamar', False)

        numero_llamen= 'Quieren que lo llamen: ' + str(llamar)

        Datos='Nombre del Restaurante: '+ request.POST["txtNombre"] +'\nCorreo: '+ request.POST["txtEmail"] + ' \nTelefono:' + request.POST["txtNumero"] + ' \nDireccion:' + request.POST["txtDomicilio"] + ' \nComentario:\n' + request.POST["txtComentario"] + '\n' + numero_llamen        
        

        email_desde=settings.EMAIL_HOST_USER
        email_para=["informatorio2020@gmail.com"]
        send_mail(nombre,Datos,email_desde,email_para,fail_silently=False)
        return render(request, "contacto_exitoso.html")

    return render(request, "restaurantes/principal.html")

def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid(): # con esto pregunto si el formulario es valido
            formulario.save()
            # Ahora lo que hago es si es correcto lo redirijo voy a importar arriba login ,authenticate
            username = formulario.cleaned_data['username'] # con .cleaned_data lo que hago es obtener los valores
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password) # con esto se autenfica ahora se hace el login
            login(request, user)
            return redirect("/principal/")
        else:
            messages.warning(request,"Ha introducido mal los valores")

    return render(request, 'registration/registrar.html', data)


