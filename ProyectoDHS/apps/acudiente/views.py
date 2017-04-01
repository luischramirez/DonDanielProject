from apps.acudiente.models import Acudiente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.acudiente.forms import FormularioAcudiente
# Create your views here.

class RegistrarAcudiente(CreateView):
    """
    Clase encargada de registrar el acudiente en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Acudiente
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioAcudiente
    #se indica que template va a gestionar el registro
    template_name = 'acudiente/pagRegistroAcudiente.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('acudiente:listar_acudiente')

class ActualizarInformacionAcudiente(UpdateView):
    """
    Clase encargada de actualizar la información del acudiente en la base de datos
    """
    #se ingresa qué modelo se utilizará para la actualización de la información
    model = Acudiente
    #se indica que formulario va a dar soporte a la acción de actualización de la información
    form_class = FormularioAcudiente 
    #se indica que template va a gestionar el registro
    #template_name =
    #se indica cual será la url de finalización
    success_url= reverse_lazy('acudiente:listar_acudiente')

class EliminarAcudiente(DeleteView):
    """
    Clase encargada de eliminar el acudiente de la base de datos
    """
    #se ingresa qué modelo se utilizará para el borrado de acudiente
    model = Acudiente
    #se indica que template va a gestionar el borrado
    #template_name =
    #se indica cual será la url de finalización
    success_url=reverse_lazy('acudiente:listar_acudiente')

class ListarAcudiente(ListView):
    """
    Clase encargada de listar los acudientes de la base de datos
    """
    #se ingresa qué modelo se utilizará para listar los acudientes
    model = Acudiente
    #se indica que template va a gestionar el listador de los acudientes
    template_name = 'acudiente/pagListaAcudiente.html'
