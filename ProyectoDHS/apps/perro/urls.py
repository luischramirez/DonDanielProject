from django.conf.urls import url
from apps.perro.views import RegistrarPerro
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$',login_required(RegistrarPerro.as_view()), name='registrar_perro'),
]
