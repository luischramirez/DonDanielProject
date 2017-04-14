from django.conf.urls import url
from apps.reserva.views import RegistrarReserva, ListarReserva, ActualizarInformacionReserva, EliminarReserva
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$',login_required(RegistrarReserva.as_view()), name='registrar_reserva'),
    url(r'^listar$',login_required(ListarReserva.as_view()), name='listar_reserva'),
    url(r'^actualizar/(?P<pk>\d+)/$',login_required(ActualizarInformacionReserva.as_view()), name='actualizar_reserva'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(EliminarReserva.as_view()), name='eliminar_reserva'),
]
