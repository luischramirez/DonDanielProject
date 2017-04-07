from django import forms
from apps.perro.models import Perro

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
            'fecha_desparacitacion',
            'epoca_celo_aproximada',
            'epoca_celo_real',
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
        ]
        labels = {
            'nombre': 'Nombre del perro',
            'fecha_nacimiento': 'Fecha nacimiento',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'peso': 'Peso',
            'estado_salud': 'Estado de salud',
            'fecha_desparacitacion': 'Fecha de desparasitación',
            'epoca_celo_aproximada': 'Época de celo aproximada',
            'epoca_celo_real': 'Época de celo real',
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
        }

        widgets = { 
            'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'nombre'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control', 'id':'fecha_nacimiento'}),
            'edad': forms.TextInput(attrs={'class':'form-control', 'id':'edad'}),
            'peso': forms.NumberInput(attrs={'class':'form-control','id':'peso'}),
            'sexo': forms.TextInput(attrs={'class':'form-control','id':'sexo','max_length':'1','placeholder':'M o H'}),
            'estado_salud': forms.TextInput(attrs={'class':'form-control', 'id':'estado_salud'}),
            'fecha_desparacitacion': forms.TextInput(attrs={'class':'form-control', 'id':'fecha_desparacitacion'}),
            'epoca_celo_aproximada': forms.DateTimeInput(attrs={'class':'form-control', 'id':'estado_salud'}),
            'epoca_celo_real': forms.DateInput(attrs={'class':'form-control', 'id':'estado_salud'}),
            'condiciones_prestamo': forms.TextInput(attrs={'class':'form-control', 'id':'condiciones_prestamo'}),
            'id_color': forms.TextInput(attrs={'class':'form-control', 'id':'color'}),
            'id_raza': forms.TextInput(attrs={'class':'form-control'}),
            'id_veterinario': forms.TextInput(attrs={'class':'form-control'}),
            'id_dieta': forms.TextInput(attrs={'class':'form-control'}),
            'id_nivel': forms.TextInput(attrs={'class':'form-control'}),
            'id_padre': forms.TextInput(attrs={'class':'form-control'}),
            'id_madre': forms.TextInput(attrs={'class':'form-control'}),
            'id_estado_perruno': forms.TextInput(attrs={'class':'form-control'}),
            'id_acudiente': forms.TextInput(attrs={'class':'form-control'}),
            'id_tamanio': forms.TextInput(attrs={'class':'form-control'}),
            'suplemento': forms.TextInput(attrs={'class':'form-control'}),
        }

