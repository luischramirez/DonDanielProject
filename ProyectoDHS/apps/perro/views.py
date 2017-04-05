from apps.perro.forms import FormularioPerro
from apps.perro.models import Perro
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
# Create your views here.

class RegistrarPerro(CreateView):
    """
    Clase encargada de registrar el perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Perro
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioPerro
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroPerro.html'
    #se indica cual será la url de finalización
    #success_url= reverse_lazy('acudiente:listar_acudiente')