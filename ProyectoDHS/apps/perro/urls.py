from django.conf.urls import url
from apps.perro.views import RegistrarPerro

urlpatterns = [
    url(r'^registrar$',RegistrarPerro.as_view(), name='registrar_perro'),
]
