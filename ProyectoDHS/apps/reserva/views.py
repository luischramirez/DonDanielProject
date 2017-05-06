from apps.reserva.forms import FormularioReserva
from apps.reserva.models import Reserva
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
# Create your views here.

class RegistrarReserva(CreateView):
    """
    Clase encargada de registrar la reserva de un perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Reserva
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioReserva
    #se indica que template va a gestionar el registro
    template_name = 'reserva/pagRegistroReserva.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('reserva:listar_reserva')

class ListarReserva(ListView):
    """
    Clase encargada de listar las reserva de los perros
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Reserva
    #se indica que template va a gestionar el registro
    template_name = 'reserva/pagListarReserva.html'

class ActualizarInformacionReserva(UpdateView):
    """
    Clase encargada de actualizar la información de las reservas de un perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Reserva
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioReserva
    #se indica que template va a gestionar el registro
    template_name = 'reserva/pagActualizarReserva.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('reserva:listar_reserva')


class EliminarReserva(DeleteView):
    """
    Clase encargada de eliminar la reserva
    """
    #se ingresa qué modelo se utilizará para el borrado de acudiente
    model = Reserva
    #se indica que template va a gestionar el borrado
    template_name = 'reserva/pagEliminarReserva.html'
    #se indica cual será la url de finalización
    success_url=reverse_lazy('reserva:listar_reserva')