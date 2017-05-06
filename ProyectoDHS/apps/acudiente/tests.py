from django.test import TestCase
import sys
#pylint:disable=E0401
from apps.acudiente.models import Acudiente

# Create your tests here.
class AcudienteTestCase(TestCase):
    """
    Clase encargada de probar las funcionalidades de: registro, actualización, borrado y consulta de Acudientes
    """
    def setUp(self):
        """
        Función encargada de setear los variables necesarios para realizar las pruebas
        """

        #sys.path
        Acudiente.objects.create(nombre='Fernando', direccion='barrio ciudad dorada', telefono='1234', email='fer@gmail.com', alias='Fer')

        Acudiente.objects.create(nombre='Fernando',direccion="barrio ciudad dorada", telefono="7357490",email="fer@gmail.com", alias="fer")



    def test_verificar_registro_acudiente(self):
        """
        Función encargada de verificar si se registró correctamente el acudiente
        """
        acudiente1 = Acudiente.objects.get(nombre='Fernando')

        acudiente1 = Acudiente.objects.get(nombre="Fernando")
        self.assertTrue(acudiente1) 
