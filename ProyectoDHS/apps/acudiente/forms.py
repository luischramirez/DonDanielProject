from django import forms
from apps.acudiente.models import Acudiente

class FormularioAcudiente(forms.ModelForm):
    """
        Clase encargada de describir el formulario para gestionar los acudientes
    """
    class Meta:
        model = Acudiente

        fields = [
            'nombre',
            'direccion',
            'telefono',
            'email',
            'alias',
        ]
        labels = {
            'nombre': 'Nombre del acudiente',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email':'E-Mail',
            'alias':'Alias',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'alias': forms.TextInput(attrs={'class':'form-control'}),
        }

