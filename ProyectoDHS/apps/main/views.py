from django.shortcuts import render
from apps.perro.models import Perro, Reserva
# Create your views here.
def index(request):
    perro = Perro.objects.all()
    reserva = Reserva.objects.all()
    #acudiente = Acudiente.objects.raw('SELECT id , nombre FROM "Acudiente"')
    contexto = {"perros" : perro, "reservas": reserva}
    #renderizo o muestro la plantilla de mascotas que tengo
    return render(request, 'main/index.html', contexto)

