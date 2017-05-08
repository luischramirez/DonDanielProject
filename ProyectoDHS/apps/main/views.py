from django.shortcuts import render
from apps.perro.models import Perro, Acudiente
# Create your views here.
def index(request):
    perro = Perro.objects.all()
    #acudiente = Acudiente.objects.raw('SELECT id , nombre FROM "Acudiente"')
    contexto = {"perros" : perro}
    #renderizo o muestro la plantilla de mascotas que tengo
    return render(request, 'main/index.html', contexto)

