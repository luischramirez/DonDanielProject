from django.db import models

    
class Acudiente(models.Model):
    """
    Clase encargada de representar el acudiente del perro 
    """
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    email = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Acudiente'


class Alimentacion(models.Model):
    """
    Clase encargada de representar la alimentación del perro 
    """
    unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='unidad_medida')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'Alimentacion'


class Color(models.Model):
    """
    Clase encargada de representar el color del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Color'


class Dia(models.Model):
    """
    Clase encargada de representar el dia de alimentación del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Dia'


class Dieta(models.Model):
    """
    Clase encargada de representar la dieta del perro 
    """
    tipo_dieta = models.ForeignKey('TipoDieta', models.DO_NOTHING, db_column='tipo_dieta')

    def __str__(self):
        return self.tipo_dieta

    class Meta:
        managed = False
        db_table = 'Dieta'


class Ejercicio(models.Model):
    """
    Clase encargada de representar los ejercicios para adiestramiento del perro 
    """
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Ejercicio'


class EstadoPerruno(models.Model):
    """
    Clase encargada de representar el estado del perro (reservado, apto para rescate, apto para busqueda) 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Estado_perruno'


class HorarioDieta(models.Model):
    """
    Clase encargada de representar el horario de la dieta de un perro 
    """
    id_dieta = models.ForeignKey(Dieta, models.DO_NOTHING, db_column='id_dieta', blank=True, null=True)
    id_alimentacion = models.ForeignKey(Alimentacion, models.DO_NOTHING, db_column='id_alimentacion')
    id_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='id_dia')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'Horario_dieta'


class Madre(models.Model):
    """
    Clase encargada de representar la madre de un perro 
    """
    id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='id_raza')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    nombre = models.TextField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Madre'


class NivelEntrenamiento(models.Model):
    """
    Clase encargada de representar el nivel de entrenamiento de un perro 
    """
    nombre = models.TextField()
    tiempo_entrenamiento = models.IntegerField()
    ejercicios = models.ManyToManyField(Ejercicio)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Nivel_entrenamiento'


class Padre(models.Model):
    """
    Clase encargada de representar el padre del perro 
    """
    id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='id_raza')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    nombre = models.TextField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Padre'

class Suplemento(models.Model):
    """
    Clase encargada de representar el suplemento que se le da a un perro 
    """
    nombre = models.TextField()
    marca = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Suplemento'      


class Vacuna(models.Model):
    """
    Clase encargada de representar la vacuna del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Vacuna'

class Perro(models.Model):
    """
    Clase encargada de representar un perro 
    """
    nombre = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    estado_salud = models.TextField(blank=True, null=True)
    fecha_desparasitacion = models.DateField(blank=True, null=True)
    epoca_celo_aproximada = models.DateField(blank=True, null=True)
    epoca_celo_real = models.DateField(blank=True, null=True)
    condiciones_prestamo = models.TextField(blank=True, null=True)
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color', blank=True, null=True)
    id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='id_raza', blank=True, null=True)
    id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='id_veterinario', blank=True, null=True)
    id_dieta = models.ForeignKey(Dieta, models.DO_NOTHING, db_column='id_dieta', blank=True, null=True)
    id_nivel_entrenamiento = models.ForeignKey(NivelEntrenamiento, models.DO_NOTHING, db_column='id_nivel_entrenamiento', blank=True, null=True)
    id_padre = models.ForeignKey(Padre, models.DO_NOTHING, db_column='id_padre', blank=True, null=True)
    id_madre = models.ForeignKey(Madre, models.DO_NOTHING, db_column='id_madre', blank=True, null=True)
    id_estado_perruno = models.ForeignKey(EstadoPerruno, models.DO_NOTHING, db_column='id_estado_perruno', blank=True, null=True)
    id_acudiente = models.ForeignKey(Acudiente, models.DO_NOTHING, db_column='id_acudiente', blank=True, null=True)
    id_tamanio = models.ForeignKey('Tamanio', models.DO_NOTHING, db_column='id_tamanio', blank=True, null=True)
    suplemento = models.ManyToManyField(Suplemento)
    vacuna = models.ManyToManyField(Vacuna)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Perro'

class Reserva(models.Model):
    """
    Clase encargada de representar la reserva de un perro 
    """
    tipo_reserva = models.ForeignKey('TipoReserva', models.DO_NOTHING, db_column='tipo_reserva')
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tiempo_estadia = models.IntegerField(blank=True, null=True)
    precio_aproximado = models.IntegerField(blank=True, null=True)
    perro = models.ManyToManyField(Perro)

    class Meta:
        managed = False
        db_table = 'Reserva'

class VacunaPerro(models.Model):
    """
    Clase encargada de representar la asociación entre vacuna y perro 
    """
    id_vacuna = models.ForeignKey(Vacuna, models.DO_NOTHING, db_column='id_vacuna', blank=True, null=True)
    id_perro = models.ForeignKey(Perro, models.DO_NOTHING, db_column='id_perro', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    vacuna_aplicada = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Vacuna_perro'
        
class Raza(models.Model):
    """
    Clase encargada de representar la raza del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Raza'


class Tamanio(models.Model):
    """
    Clase encargada de representar el tamaño del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Tamanio'


class TipoDieta(models.Model):
    """
    Clase encargada de representar el tipo de dieta del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Tipo_dieta'


class TipoReserva(models.Model):
    """
    Clase encargada de representar el tipo de reserva al cual un perro está asociado. (adiestramiento, crianza, guarderia) 
    """
    nombre = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Tipo_reserva'


class UnidadMedida(models.Model):
    """
    Clase encargada de representar la unidad de medida de la alimentación del perro 
    """
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Unidad_medida'

class Veterinario(models.Model):
    """
    Clase encargada de representar el veterinario del perro 
    """
    nombre = models.TextField()
    telefono = models.TextField()
    direccion = models.TextField()
    email = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
        
    class Meta:
        managed = False
        db_table = 'Veterinario'