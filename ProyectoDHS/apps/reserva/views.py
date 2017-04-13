from apps.reserva.forms import FormularioReserva
from apps.reserva.models import Reserva
from apps.reserva.models import TipoReserva
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
# Create your views here.

class RegistrarReserva(CreateView):
    """
    Clase encargada de registrar el perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Reserva
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioReserva
    #se indica que template va a gestionar el registro
    template_name = 'reserva/pagRegistroReserva.html'
    #se indica cual será la url de finalización
    #success_url= reverse_lazy('acudiente:listar_acudiente')