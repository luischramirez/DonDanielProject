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
            'nombre': 'Nombre completo del acudiente',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email':'E-Mail',
            'alias':'Alias',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Escriba el nombre completo del acudiente'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','id':'dir','placeholder':'Ej: Calle 20 # 38 Sur - 15 Armenia'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','id':'tel','placeholder':'Ej: 3208543680'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'correo','type':'email','placeholder':'ejemplo@mail.com'}),
            'alias': forms.TextInput(attrs={'class':'form-control','id':'apodo','placeholder':'Escriba el apodo del acudiente'}),
        }