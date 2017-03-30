from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Acudiente(models.Model):
    
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    email = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Acudiente'


class Alimentacion(models.Model):
    unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='unidad_medida')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'Alimentacion'


class Color(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Color'


class Dia(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Dia'


class Dieta(models.Model):
    tipo_dieta = models.ForeignKey('TipoDieta', models.DO_NOTHING, db_column='tipo_dieta')

    class Meta:
        managed = False
        db_table = 'Dieta'


class Ejercicio(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'Ejercicio'


class EjercicioIntermedio(models.Model):
    id_ejercicio = models.ForeignKey(Ejercicio, models.DO_NOTHING, db_column='id_ejercicio')
    id_nivel_entrenamiento = models.ForeignKey('NivelEntrenamiento', models.DO_NOTHING, db_column='id_nivel_entrenamiento')
    tiempo_entrenamiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Ejercicio_intermedio'


class EstadoPerruno(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Estado_perruno'


class HorarioDieta(models.Model):
    id_dieta = models.ForeignKey(Dieta, models.DO_NOTHING, db_column='id_dieta', blank=True, null=True)
    id_alimentacion = models.ForeignKey(Alimentacion, models.DO_NOTHING, db_column='id_alimentacion')
    id_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='id_dia')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'Horario_dieta'


class Madre(models.Model):
    id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='id_raza')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    nombre = models.TextField()
    edad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Madre'


class NivelEntrenamiento(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Nivel_entrenamiento'


class Padre(models.Model):
    id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='id_raza')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    nombre = models.TextField()
    edad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Padre'


class ProductoAseo(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Producto_aseo'

class Suplemento(models.Model):
    nombre = models.TextField()
    marca = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Suplemento'        


class Perro(models.Model):
    nombre = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    estado_salud = models.TextField(blank=True, null=True)
    fecha_desparacitacion = models.DateField(blank=True, null=True)
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
    producto_aseo = models.ManyToManyField(ProductoAseo)
    suplemento = models.ManyToManyField(Suplemento)

    class Meta:
        managed = False
        db_table = 'Perro'


class Raza(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Raza'


class Reserva(models.Model):
    tipo_reserva = models.ForeignKey('TipoReserva', models.DO_NOTHING, db_column='tipo_reserva')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'Reserva'


class ReservaIntermedia(models.Model):
    id_perro = models.ForeignKey(Perro, models.DO_NOTHING, db_column='id_perro', blank=True, null=True)
    id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='id_reserva', blank=True, null=True)
    precio_aproximado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reserva_intermedia'


class Tamanio(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tamanio'


class TipoDieta(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_dieta'


class TipoReserva(models.Model):
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tipo_reserva'


class TipoServicio(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_servicio'


class TipoServicioPerro(models.Model):
    fecha_entrada = models.DateField(blank=True, null=True)
    tiempo_estadia = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    precio_aproximado = models.IntegerField(blank=True, null=True)
    id_tipo_servicio = models.ForeignKey(TipoServicio, models.DO_NOTHING, db_column='id_tipo_servicio', blank=True, null=True)
    id_perro = models.ForeignKey(Perro, models.DO_NOTHING, db_column='id_perro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tipo_servicio_perro'


class UnidadMedida(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Unidad_medida'


class Vacuna(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Vacuna'


class VacunaPerro(models.Model):
    id_vacuna = models.ForeignKey(Vacuna, models.DO_NOTHING, db_column='id_vacuna', blank=True, null=True)
    id_perro = models.ForeignKey(Perro, models.DO_NOTHING, db_column='id_perro', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    vacuna_aplicada = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Vacuna_perro'


class Veterinario(models.Model):
    nombre = models.TextField()
    telefono = models.TextField()
    direccion = models.TextField()
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Veterinario'
