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

    def test_verificar_eliminado_acudiente(self):
        """
        Función encargada de verificar si se elimina correctamente un acudiente
        """
        #pylint: disable=E1101
        acudiente1 = Acudiente.objects.get(nombre='Fernando')
        acudiente1.delete()
        self.assertFalse(Acudiente.objects.get(nombre='Fernando'))    

    def test_verificar_actualizacion_acudiente(self):
        """
        Función encargada de verificar si se actualizan correctamente los datos del acudiente
        """
        #pylint: disable=E1101
        acudiente1 = Acudiente.objects.get(nombre='Fernando')
        acudiente1.nombre='Joaquin'
        self.assertEqual('Joaquin',acudiente1.nombre)
    
    def test_verificar_consulta_acudiente(self):
        """
        Función encargada de verificar si se consulta correctamente los datos del acudiente
        """
        #pylint: disable=E1101
        acudiente1 = Acudiente.objects.all()
        self.assertTrue(acudiente1)