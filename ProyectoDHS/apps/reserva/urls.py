from django.conf.urls import url
from apps.reserva.views import RegistrarReserva
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$',login_required(RegistrarReserva.as_view()), name='registrar_reserva'),
]
