from django.conf.urls import url
from apps.main.views import index
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^index$',login_required(index), name='index'),
]
