from django.contrib import admin
from apps.restaurantes.models import Comentario,Restaurant,ComentarioSurtidor,ComentarioLomo,ComentarioChimenea,ComentarioNanas,ComentarioJose
admin.site.register(Comentario)
admin.site.register(ComentarioSurtidor)
admin.site.register(ComentarioLomo)
admin.site.register(ComentarioChimenea)
admin.site.register(ComentarioNanas)
admin.site.register(ComentarioJose)
admin.site.register(Restaurant)

# Register your models here.