from django.test import TestCase
from apps.reserva.models import Reserva
# Create your tests here.

# Create your tests here.
class ReservaTestCase(TestCase):
    """
    Clase encargada de probar las funcionalidades de: registro,
    actualización, borrado y consulta de Reservas
    """
    def setUp(self):
        """
        Función encargada de establecer los datos necesarios para realizar las pruebas
        """
        #pylint: disable=E1101
        Reserva.objects.create(tipo_reserva='Adiestramiento', fecha_entrada='10/02/2018', fecha_salida='10/03/2018', tiempo_estadia='27', precio_aproximado='300000',perro='Bruno')

    def test_verificar_registro_reserva(self):
        """
        Función encargada de verificar si se registró correctamente la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Bruno')
        self.assertTrue(reserva1)

    def test_verificar_eliminado_reserva(self):
        """
        Función encargada de verificar si se elimina correctamente una reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Bruno')
        reserva1.delete()
        self.assertFalse(Reserva.objects.get(perro='Bruno'))    

    def test_verificar_actualizacion_reserva(self):
        """
        Función encargada de verificar si se actualizan correctamente los datos de la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Bruno')
        reserva1.precio_aproximado='475600'
        self.assertEqual('475600',reserva1.precio_aproximado)
    
    def test_verificar_consulta_reserva(self):
        """
        Función encargada de verificar si se consulta correctamente los datos de la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.all()
        self.assertTrue(reserva1)