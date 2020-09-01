from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    doc_externo=open("C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/index.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre_persona"})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def principal(request):
    doc_externo=open("C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/principal.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre_persona"})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def restaurante(request):
    doc_externo=open("C:/Users/Luis/Desktop/Aplicacion/Loquepinte/Loquepinte/plantillas/restaurante.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre_persona"})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)