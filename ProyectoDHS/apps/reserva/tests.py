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
        Reserva.objects.create(tipo_reserva='Guarderia', fecha_entrada='10/02/2018', fecha_salida='10/03/2018', tiempo_estadia='27', precio_aproximado='300000',perro='Kira')

    def test_verificar_registro_reserva(self):
        """
        Función encargada de verificar si se registró correctamente la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Kira')
        self.assertTrue(reserva1)

    def test_verificar_eliminado_reserva(self):
        """
        Función encargada de verificar si se elimina correctamente una reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Kira')
        reserva1.delete()
        self.assertFalse(Reserva.objects.get(perro='Kira'))    

    def test_verificar_actualizacion_reserva(self):
        """
        Función encargada de verificar si se actualizan correctamente los datos de la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.get(perro='Kira')
        reserva1.tipo_reserva='Adiestramiento'
        self.assertEqual('Adiestramiento',reserva1.tipo_reserva)
    
    def test_verificar_consulta_reserva(self):
        """
        Función encargada de verificar si se consulta correctamente los datos de la reserva
        """
        #pylint: disable=E1101
        reserva1 = Reserva.objects.all()
        self.assertTrue(reserva1)