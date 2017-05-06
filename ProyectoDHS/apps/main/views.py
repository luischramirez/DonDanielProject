from django.shortcuts import render
"""from gi.repository import Notify
from apps.main.models import Alimentacion, Perro"""

# Create your views here.
def index(request):
    #renderizo o muestro la plantilla de mascotas que tengo
    return render(request, 'main/index.html')

"""Notify.init("main")

def notify():
    
    notification_comida = Notify.Notification.new("Default Title", "Default Body")

    notification_comida.update("Hello","World!")
    

if __name__ == '__main__':
    notify()
"""