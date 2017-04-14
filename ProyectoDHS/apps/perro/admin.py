from django.contrib import admin
from apps.perro.models import Perro, NivelEntrenamiento, Ejercicio
# Register your models here.
admin.site.register(Perro)
admin.site.register(NivelEntrenamiento)
admin.site.register(Ejercicio)