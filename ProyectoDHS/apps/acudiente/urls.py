from django.conf.urls import url
from apps.acudiente.views import RegistrarAcudiente, ActualizarInformacionAcudiente, EliminarAcudiente,ListarAcudiente

urlpatterns = [
    url(r'^registrar$',RegistrarAcudiente.as_view(), name='registrar_acudiente'),
    url(r'^actualizar/(?P<pk>\d+)/$',ActualizarInformacionAcudiente.as_view(), name='actualizar_acudiente'),
    url(r'^eliminar/(?P<pk>\d+)/$',EliminarAcudiente.as_view(), name='eliminar_acudiente'),
    url(r'^listar$',ListarAcudiente.as_view(),name='listar_acudiente'),
]
