from django.test import TestCase
#pylint:disable=E0401
from apps.acudiente.models import Raza

# Create your tests here.
class AcudienteTestCase(TestCase):
    """
    Clase encargada de probar las funcionalidades de: registro, actualización, borrado y consulta de Acudientes
    """
    def setUp(self):
        """
        Función encargada de setear los variables necesarios para realizar las pruebas
        """
        #Acudiente.objects.create(nombre='Fernando')


    def test_verificar_registro_acudiente(self):
        """
        Función encargada de verificar si se registró correctamente el acudiente
        """
        acudiente1 = Raza.objects.get(id=1)
        self.assertTrue(acudiente1) 
