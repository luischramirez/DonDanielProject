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
        Perro.objects.create(nombre='toby', fecha_nacimiento='17/02/2010',
        edad='8', sexo='M', peso='10',estado_salud='sano',fecha_desparasitacion='',
        epoca_celo_aproximada='', epoca_celo_real='',condiciones_prestamo='',id_color='1',
        id_raza='10',id_veterinario='', id_nivel_entrenamiento='1', id_padre='',id_madre='',
        id_estado_perruno='2',id_acudiente='1', id_tamanio='1',suplemento='',vacuna='',horario_dieta='1')


    def test_verificar_registro_perro(self):
        """
        Función encargada de verificar si se registró correctamente el perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='toby')
        self.assertTrue(perro1)

    def test_verificar_eliminado_perro(self):
        """
        Función encargada de verificar si se elimina correctamente un perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='toby')
        perro1.delete()
        self.assertFalse(Perro.objects.get(nombre='Toby'))    

    def test_verificar_actualizacion_perro(self):
        """
        Función encargada de verificar si se actualizan correctamente los datos del perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.get(nombre='toby')
        perro1.nombre='Lucas'
        self.assertEqual('Lucas',perro1.nombre)
    
    def test_verificar_consulta_perro(self):
        """
        Función encargada de verificar si se consulta correctamente los datos del perro
        """
        #pylint: disable=E1101
        perro1 = Perro.objects.all()
        self.assertTrue(perro1)
