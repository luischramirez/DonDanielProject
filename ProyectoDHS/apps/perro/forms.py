from django import forms
from apps.perro.models import Perro, Veterinario, Madre, Padre, Suplemento,NivelEntrenamiento


class FormularioPerro(forms.ModelForm):
    """
        Clase encargada de describir el formulario para gestionar los perros
    """

    class Meta:
        model = Perro

        fields = [
            'nombre',
            'fecha_nacimiento',
            'edad',
            'sexo',
            'peso',
            'estado_salud',
            'fecha_desparasitacion',
            'epoca_celo_real',
            'epoca_celo_aproximada',
            'condiciones_prestamo',
            'id_color',
            'id_raza',
            'id_veterinario',
            'id_dieta',
            'id_nivel_entrenamiento',
            'id_padre',
            'id_madre',
            'id_estado_perruno',
            'id_acudiente',
            'id_tamanio',
            'suplemento',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre del perro',
            'fecha_nacimiento': 'Fecha nacimiento',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'peso': 'Peso',
            'estado_salud': 'Estado de salud',
            'fecha_desparasitacion': 'Fecha de desparasitación',
            'epoca_celo_real': 'Época de celo real',
            'epoca_celo_aproximada': 'Época de celo aproximada',
            'condiciones_prestamo': 'Condiciones de préstamo',
            'id_color': 'Color',
            'id_raza': 'Raza',
            'id_veterinario': 'Veterinario',
            'id_dieta': 'Dieta',
            'id_nivel_entrenamiento': 'Nivel de entrenamiento',
            'id_padre': 'Padre',
            'id_madre': 'Madre',
            'id_estado_perruno': 'Estado perruno',
            'id_acudiente': 'Acudiente',
            'id_tamanio': 'Tamaño',
            'suplemento': 'Suplementos',
            'vacuna': 'Vacunas',
        }

        widgets = { 
            'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'fecha_nacimiento'}),
            'edad': forms.TextInput(attrs={'class':'form-control', 'id':'edad','disabled':'true'}),
            'peso': forms.NumberInput(attrs={'class':'form-control','id':'peso','placeholder':'Número del peso en gramos'}),
            'sexo': forms.TextInput(attrs={'class':'form-control','id':'sexo','max_length':'1','placeholder':'M o H'}),
            'fecha_desparasitacion': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'fecha_desparasitacion'}),
            'estado_salud': forms.TextInput(attrs={'class':'form-control', 'id':'estado_salud','placeholder':'Condiciones en las que se recibe al canino'}),
            'epoca_celo_real': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_real'}),
            'epoca_celo_aproximada': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_aprox','disabled':'true'}),
            'condiciones_prestamo': forms.TextInput(attrs={'class':'form-control', 'id':'condiciones_prestamo','placeholder':'Condiciones pautadas con el dueño del canino'}),
            'id_color': forms.Select(attrs={'class':'form-control', 'id':'color'}),
            'id_raza': forms.Select(attrs={'class':'form-control'}),
            'id_veterinario': forms.Select(attrs={'class':'form-control','id':'veterinario'}),
            'id_dieta': forms.Select(attrs={'class':'form-control','id':'dieta'}),
            'id_nivel_entrenamiento': forms.Select(attrs={'class':'form-control','id':'nivel'}),
            'id_padre': forms.Select(attrs={'class':'form-control','id':'padre'}),
            'id_madre': forms.Select(attrs={'class':'form-control','id':'madre'}),
            'id_estado_perruno': forms.Select(attrs={'class':'form-control'}),
            'id_acudiente': forms.Select(attrs={'class':'form-control'}),
            'id_tamanio': forms.Select(attrs={'class':'form-control'}),
            'suplemento': forms.CheckboxSelectMultiple(attrs={'id':'suplemento'}),
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
            'telefono':forms.TextInput(attrs={'class':'form-control', 'id':'telefono','placeholder':'Teléfono'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'id':'dirección','placeholder':'Dirección'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'id':'email','placeholder':'E-Mail'}),
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
            'edad':forms.TextInput(attrs={'class':'form-control', 'id':'edad','placeholder':'Edad'}),
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
            'edad':forms.TextInput(attrs={'class':'form-control', 'id':'edad','placeholder':'Edad'}),
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
            'ejercicio',
        ]
        labels={
            'nombre':'Nombre',
            'tiempo_entrenamiento':'Tiempo de entrenamiento',
            'ejercicio':'Ejercicios',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre','placeholder':'Nombre'}),
            'tiempo_entrenamiento':forms.NumberInput(attrs={'class':'form-control', 'id':'tiempo_entreno','placeholder':'Tiempo de entrenamiento (en días)'}),
            'ejercicio':forms.CheckboxSelectMultiple(),
        }
