from django.test import TestCase
from apps.perro.models import Perro
# Create your tests here.
class PerroTestCase(TestCase):
    """
    Clase encargada de probar las funcionalidades de: registro,
    actualización, borrado y consulta de perros
    """
    def setUp(self):
        """
        Función encargada de establecer los datos necesarios para realizar las pruebas
        """

        #sys.path
        #pylint: disable=E1101
        Perro.objects.create(nombre='Sasha', fecha_nacimiento='2010-02-17',
        edad='8', sexo='H', peso='10',estado_salud='sana',fecha_desparasitacion='2017-06-20',
        epoca_celo_aproximada='2018-02-17', epoca_celo_real='2017-08-17',condiciones_prestamo='',id_color=1,
        id_raza=3,id_veterinario=None, id_nivel_entrenamiento=2, id_padre=None,id_madre=None,
        id_estado_perruno=1,id_acudiente=1, id_tamanio=1)


    def test_verificar_registro_perro(self):
        """
        Función encargada de verificar si se registró correctamente el perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='Sasha')
        self.assertTrue(perro1)

    def test_verificar_eliminado_perro(self):
        """
        Función encargada de verificar si se elimina correctamente un perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='Sasha')
        perro1.delete()
        self.assertFalse(Perro.objects.get(nombre='Sasha'))    

    def test_verificar_actualizacion_perro(self):
        """
        Función encargada de verificar si se actualizan correctamente los datos del perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='Sasha')
        perro1.nombre='Niña'
        self.assertEqual('Niña',perro1.nombre)
    
    def test_verificar_consulta_perro(self):
        """
        Función encargada de verificar si se consulta correctamente los datos del perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.all()
        self.assertTrue(perro1)
