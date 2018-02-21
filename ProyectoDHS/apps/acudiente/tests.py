from django.test import TestCase
from apps.acudiente.models import Acudiente

# Create your tests here.
class AcudienteTestCase(TestCase):
    """
    Clase encargada de probar las funcionalidades de: registro,
    actualización, borrado y consulta de Acudientes
    """
    def setUp(self):
        """
        Función encargada de establecer los datos necesarios para realizar las pruebas
        """
        #pylint: disable=E1101
        Acudiente.objects.create(nombre='Fernando', direccion='barrio ciudad dorada', telefono='1234', email='fer@gmail.com', alias='Fer')

    def test_verificar_registro_acudiente(self):
        """
        Función encargada de verificar si se registró correctamente el acudiente
        """
        #pylint: disable=E1101
        acudiente1 = Acudiente.objects.get(nombre='Fernando')
        self.assertTrue(acudiente1)
