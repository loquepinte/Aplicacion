"""Loquepinte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include  # aca tambien agreger ver despues si esto no es que me tira
from django.contrib.auth.decorators import login_required
from Loquepinte.views import home,principal,restaurante,contactar, registro_usuario
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('principal/', principal),
    path('restaurante/', restaurante),
    path('contactar/', contactar),
    path('accounts/', include('django.contrib.auth.urls' )), # esto trae la ruta del login, la del log out, etc
    path('registrar/',registro_usuario,name = 'registro_usuario')
]

