from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserForm, Comment, Restaurant, Comentario,ComentarioSurtidor,ComentarioLomo,ComentarioChimenea,ComentarioNanas,ComentarioJose
from django.shortcuts import render, redirect, get_object_or_404 # ademas del render coloco el redirect para redireccionar
from django.contrib.auth.decorators import login_required # este sirve para obligar que este logeado para ingresar
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def principal(request):
    return render(request, "restaurantes/principal.html")

def restaurante(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = Comentario.objects.all().order_by('-id')[:3]
    comentarios = Comentario.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
    return render(request, "restaurantes/restaurante.html", contexto)

def el_surtidor(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioSurtidor.objects.all().order_by('-id')[:3]
    comentarios = ComentarioSurtidor.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
    return render(request, "restaurantes/el_surtidor.html", contexto)

def el_patron(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioLomo.objects.all().order_by('-id')[:3]
    comentarios = ComentarioLomo.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
    return render(request, "restaurantes/el_patron.html", contexto)

def la_chimenea(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioChimenea.objects.all().order_by('-id')[:3]
    comentarios = ComentarioChimenea.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
    return render(request, "restaurantes/la_chimenea.html", contexto)
def nanas(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioNanas.objects.all().order_by('-id')[:3]
    comentarios = ComentarioNanas.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
    return render(request, "restaurantes/nanas.html", contexto)
def san_jose(request):
    '''Este función retorna la lista de comentarios de nuestra base de datos
    y los ordena de mayor a menor, trayendo solo los ultimos 3 ids'''
    Ultimoscomentarios = ComentarioJose.objects.all().order_by('-id')[:3]
    comentarios = ComentarioJose.objects.all().order_by('-id')
    
    contexto={
        'comentario':Ultimoscomentarios, 'comentarios':comentarios,
    } 
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
            return render(request, "restaurantes/principal.html")
        else:
            return render(request, "registration/error_registro.html")
    return render(request, 'registration/registrar.html', data)

def error(request):
    return render(request, "registration/error_registro.html")


@login_required
def comentario(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_Usuario"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=1)
        texto=request.POST["txt_Comentario"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = Comentario(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../restaurante/")
    return render(request, "comentario.html")    
@login_required
def comentarioSurtidor(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioSur"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=2)
        texto=request.POST["txt_ComentarioSur"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioSurtidor(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../el_surtidor/")
    return render(request, "comentarioSurtidor.html")
@login_required
def comentarioLomo(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioLomo"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=3)
        texto=request.POST["txt_ComentarioLomo"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioLomo(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../el_patron/")
    return render(request, "comentarioLomo.html")    
@login_required
def comentarioChimenea(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioChi"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=4)
        texto=request.POST["txt_ComentarioChi"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioChimenea(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../la_chimenea/")
    return render(request, "comentarioChimenea.html") 
@login_required
def comentarioNanas(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioNanas"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=5)
        texto=request.POST["txt_ComentarioNanas"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioNanas(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../nanas/")
    return render(request, "comentarioNanas.html")    
@login_required   
def comentarioJose(request):
    if request.method == 'POST':
        nombre_Usuario = request.POST["txt_UsuarioJo"]
        # nombre_Restaurant = request.POST["txt_Restaurant"]
        nombre_Restaurant = Restaurant.objects.get(Id=6)
        texto=request.POST["txt_ComentarioJo"]
        calificacion = "★"
        try:            
            calificacion = request.POST["estrellas"]
        except:
            None
        comentario = ComentarioJose(usuario=nombre_Usuario, Nombre_restaurant=nombre_Restaurant, mensaje=texto, valoracion=calificacion)
        comentario.save()
        return redirect("../san_jose/")
    return render(request, "comentarioJose.html")    


# def comentarios(request):
#     comentario= Comentario.objects.all().order_by('-id')
#     contexto={
#         'comentario':comentario,
#     }  
#     return render(request, "comentarios.html",contexto)




