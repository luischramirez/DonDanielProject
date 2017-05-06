from django.conf.urls import url
from apps.perro.views import RegistrarPerro,RegistrarVeterinario,RegistrarMadre,RegistrarPadre,RegistrarSuplemento,RegistrarNivelPersonalizado,RegistrarDieta,RegistrarAlimentacion,ListarPerro,ActualizarInformacionPerro,EliminarPerro
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$',login_required(RegistrarPerro.as_view()), name='registrar_perro'),
    url(r'^registrarVeterinario$',login_required(RegistrarVeterinario.as_view()), name='registrar_veterinario'),
    url(r'^registrarMadre$',login_required(RegistrarMadre.as_view()), name='registrar_madre'),
    url(r'^registrarPadre$',login_required(RegistrarPadre.as_view()), name='registrar_padre'),
    url(r'^registrarSuplemento$',login_required(RegistrarSuplemento.as_view()), name='registrar_suplemento'),
    url(r'^registrarNivelPersonalizado$',login_required(RegistrarNivelPersonalizado.as_view()), name='registrar_nivel_personalizado'),
    url(r'^registrarDieta$',login_required(RegistrarDieta.as_view()), name='registrar_dieta'),
    url(r'^registrarAlimentacion$',login_required(RegistrarAlimentacion.as_view()), name='registrar_alimentacion'),
    url(r'^listarPerro$',login_required(ListarPerro.as_view()), name='listar_perro'),
    url(r'^actualizarPerro/(?P<pk>\d+)/$',login_required(ActualizarInformacionPerro.as_view()), name='actualizar_perro'),
    url(r'^eliminarPerro/(?P<pk>\d+)/$',login_required(EliminarPerro.as_view()), name='eliminar_perro'),

]