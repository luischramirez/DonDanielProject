from django.conf.urls import url
from apps.main.views import index  
urlpatterns = [
    url(r'^index$',index , name='index'),
]
