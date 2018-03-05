from django import forms
from apps.perro.models import Perro, Veterinario, Madre, Padre, Suplemento,NivelEntrenamiento, HorarioDieta, Alimentacion

class FormularioPerro(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar los perros
    """

    class Meta:
        model = Perro

        fields = [
            'nombre',
            'id_acudiente',
            'horario_dieta',
            'id_padre',
            'id_madre',
            'id_veterinario',
            'id_nivel_entrenamiento',
            'suplemento',
            'fecha_nacimiento',
            'edad',
            'id_raza',
            'sexo',
            'peso',
            'id_tamanio',
            'id_color',
            'fecha_desparasitacion',
            'epoca_celo_real',
            'epoca_celo_aproximada',
            'id_estado_perruno',
            'estado_salud',
            'condiciones_prestamo',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre del perro',
            'id_acudiente': 'Acudiente',
            'horario_dieta': 'Dietas',
            'id_padre': 'Padre',
            'id_madre': 'Madre',
            'id_veterinario': 'Veterinario',
            'id_nivel_entrenamiento': 'Nivel de entrenamiento',
            'suplemento': 'Suplementos',
            'fecha_nacimiento': 'Fecha nacimiento',
            'edad': 'Edad',
            'id_raza': 'Raza',
            'sexo': 'Sexo',
            'peso': 'Peso',
            'id_tamanio': 'Tamaño',
            'id_color': 'Color',
            'fecha_desparasitacion': 'Fecha de desparasitación',
            'epoca_celo_real': 'Época de celo real',
            'epoca_celo_aproximada': 'Época de celo aproximada',
            'id_estado_perruno': 'Estado perruno',
            'estado_salud': 'Estado de salud',
            'condiciones_prestamo': 'Observaciones de servicio',
            'vacuna': 'Vacunas',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'id_acudiente': forms.Select(attrs={'class':'form-control'}),
            'horario_dieta': forms.CheckboxSelectMultiple(attrs={'id':'horario_dieta'}),
            'id_padre': forms.Select(attrs={'class':'form-control','id':'padre'}),
            'id_madre': forms.Select(attrs={'class':'form-control','id':'madre'}),
            'id_veterinario': forms.Select(attrs={'class':'form-control','id':'veterinario'}),
            'id_nivel_entrenamiento': forms.Select(attrs={'class':'form-control','id':'nivel'}),
            'suplemento': forms.CheckboxSelectMultiple(attrs={'id':'suplemento'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'fecha_nacimiento'}),
            'edad': forms.NumberInput(attrs={'class':'form-control', 'id':'edad','placeholder':'Es autocalculada'}),
            'id_raza': forms.Select(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control','id':'sexo','max_length':'1','placeholder':'M o H (Mayúscula)'}),
            'peso': forms.NumberInput(attrs={'class':'form-control','id':'peso','placeholder':'Número del peso en kilogramos'}),
            'id_tamanio': forms.Select(attrs={'class':'form-control'}),
            'id_color': forms.Select(attrs={'class':'form-control', 'id':'color'}),
            'fecha_desparasitacion': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'fecha_desparasitacion'}),
            'epoca_celo_real': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_real'}),
            'epoca_celo_aproximada': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_aprox','placeholder':'Es autocalculada','readonly':'readonly'}),
            'id_estado_perruno': forms.Select(attrs={'class':'form-control'}),
            'estado_salud': forms.TextInput(attrs={'class':'form-control', 'id':'estado_salud','placeholder':'Condiciones en las que se recibe al canino'}),
            'condiciones_prestamo': forms.TextInput(attrs={'class':'form-control', 'id':'condiciones_prestamo','placeholder':'Condiciones pautadas con el dueño del canino'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }

class FormularioVeterinario(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar los veterinarios
    """
    class Meta:
        model = Veterinario

        fields=[
            'nombre',
            'telefono',
            'direccion',
            'email',
        ]
        labels={
            'nombre':'Nombre',
            'telefono':'Teléfono',
            'direccion':'Dirección',
            'email':'E-Mail',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control', 'id':'telefono','placeholder':'Teléfono'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'id':'dirección','placeholder':'Dirección'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'id':'email','type':'email','placeholder':'E-Mail'}),
        }

class FormularioMadre(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar las madres de los perros
    """
    class Meta:
        model = Madre

        fields=[
            'nombre',
            'edad',
            'id_raza',
            'id_color',
        ]
        labels={
            'nombre':'Nombre',
            'edad':'Edad',
            'id_raza':'Raza',
            'id_color':'Color',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'edad':forms.NumberInput(attrs={'class':'form-control', 'id':'edad','placeholder':'Edad'}),
            'id_raza':forms.Select(attrs={'class':'form-control', 'id':'id_raza'}),
            'id_color':forms.Select(attrs={'class':'form-control', 'id':'id_color'}),
        }

class FormularioPadre(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar los padres de los perros
    """
    class Meta:
        model = Padre

        fields=[
            'nombre',
            'edad',
            'id_raza',
            'id_color',
        ]
        labels={
            'nombre':'Nombre',
            'edad':'Edad',
            'id_raza':'Raza',
            'id_color':'Color',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'edad':forms.NumberInput(attrs={'class':'form-control', 'id':'edad','placeholder':'Edad'}),
            'id_raza':forms.Select(attrs={'class':'form-control', 'id':'id_raza'}),
            'id_color':forms.Select(attrs={'class':'form-control', 'id':'id_color'}),
        }

class FormularioSuplemento(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar los suplementos de un perro
    """
    class Meta:
        model = Suplemento

        fields=[
            'nombre',
            'marca',
        ]
        labels={
            'nombre':'Nombre',
            'marca':'Marca',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'marca':forms.TextInput(attrs={'class':'form-control', 'id':'marca','placeholder':'Marca'}),
        }

class FormularioNivelPersonalizado(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar los niveles personalizados de adiestramiento de un perro
    """
    class Meta:
        model = NivelEntrenamiento

        fields=[
            'nombre',
            'tiempo_entrenamiento',
            'ejercicios',
        ]
        labels={
            'nombre':'Nombre',
            'tiempo_entrenamiento':'Tiempo de entrenamiento',
            'ejercicios':'Ejercicios',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'tiempo_entrenamiento':forms.NumberInput(attrs={'class':'form-control', 'id':'tiempo_entreno','placeholder':'Tiempo de entrenamiento (en días)'}),
            'ejercicios':forms.CheckboxSelectMultiple(),
        }

class FormularioDieta(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar la dieta de un perro
    """
    class Meta:
        model = HorarioDieta

        fields=[
            'id_alimentacion',
            'id_dia',
            'descripcion',
        ]
        labels={
            'id_alimentacion':'Alimentación',
            'id_dia':'Dia',
            'descripcion':'Descripción de la dieta',
        }
        widgets={
            'id_alimentacion':forms.Select(attrs={'class':'form-control', 'id':'alimentacion','name':'alimentacion'}),
            'id_dia':forms.Select(attrs={'class':'form-control', 'id':'dia','name':'alimentacion'}),
            'descripcion':forms.TextInput(attrs={'placeholder':'Descripción generada de la dieta','id':'descripcion_d', 'class':'form-control'}),
        }
class FormularioAlimentacion(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar la dieta de un perro
    """
    class Meta:
        model = Alimentacion

        fields=[
            'nombre',
        ]
        labels={
            'nombre':'Nombre',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Escriba el nombre del producto'}),
        }