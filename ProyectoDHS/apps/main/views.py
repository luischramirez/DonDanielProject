from django.shortcuts import render

# Create your views here.
def index(request):
    #renderizo o muestro la plantilla de mascotas que tengo
    return render(request, 'main/index.html')
