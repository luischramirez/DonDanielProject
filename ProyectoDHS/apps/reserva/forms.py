from django import forms
from apps.reserva.models import Reserva

class FormularioReserva(forms.ModelForm):
    """
    Clase encargada de describir el formulario para gestionar las reservas
    """
    class Meta:
        model = Reserva

        fields = [
            'perro',
            'tipo_reserva',
            'fecha_entrada',
            'tiempo_estadia',
            'fecha_salida',
            'precio_aproximado',
        ]
        labels = {
            'perro': 'Seleccione el perro',
            'tipo_reserva': 'Seleccione el tipo de reserva',
            'fecha_entrada': 'Fecha de entrada',
            'tiempo_estadia': 'Tiempo de estadía',
            'fecha_salida': 'Fecha de salida',
            'precio_aproximado': 'Precio aproximado',
        }
        widgets = {
            'perro': forms.Select(attrs={'class':'form-control','id':'perro'}),
            'tipo_reserva': forms.Select(attrs={'class':'form-control','id':'tipo_reserva'}),
            'fecha_entrada': forms.TextInput(attrs={'class':'datepicker form-control', 'id':'fecha_entrada'}),
            'tiempo_estadia': forms.NumberInput(attrs={'class':'form-control','id':'tiempo_estadia','placeholder':'Tiempo de estadía en días'}),
            'fecha_salida': forms.TextInput(attrs={'class':'datepicker form-control', 'id':'fecha_salida'}),
            'precio_aproximado': forms.NumberInput(attrs={'class':'form-control','id':'precio_aproximado','placeholder':'Valor a cobrar aproximado'}),
        }