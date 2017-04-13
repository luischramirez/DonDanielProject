from django.conf.urls import url
from apps.perro.views import RegistrarPerro,RegistrarVeterinario,RegistrarMadre,RegistrarPadre,RegistrarSuplemento
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$',login_required(RegistrarPerro.as_view()), name='registrar_perro'),
    url(r'^registrarVeterinario$',login_required(RegistrarVeterinario.as_view()), name='registrar_veterinario'),
    url(r'^registrarMadre$',login_required(RegistrarMadre.as_view()), name='registrar_madre'),
    url(r'^registrarPadre$',login_required(RegistrarPadre.as_view()), name='registrar_padre'),
    url(r'^registrarSuplemento$',login_required(RegistrarSuplemento.as_view()), name='registrar_suplemento'),
]
