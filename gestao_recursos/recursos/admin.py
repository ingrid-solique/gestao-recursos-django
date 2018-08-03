from django.contrib import admin
from .models import Categoria, Recurso, Reserva, ReservaRecurso, Dano, Perfil


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Recurso)
admin.site.register(Reserva)
admin.site.register(ReservaRecurso)
admin.site.register(Dano)
admin.site.register(Perfil)

