from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.acudiente.views import RegistrarAcudiente, ActualizarInformacionAcudiente, EliminarAcudiente, ListarAcudiente
urlpatterns = [
    url(r'^registrar$',login_required(RegistrarAcudiente.as_view()), name='registrar_acudiente'),
    url(r'^actualizar/(?P<pk>\d+)/$',login_required(ActualizarInformacionAcudiente.as_view()), name='actualizar_acudiente'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(EliminarAcudiente.as_view()), name='eliminar_acudiente'),
    url(r'^listar$',login_required(ListarAcudiente.as_view()),name='listar_acudiente'),
]
