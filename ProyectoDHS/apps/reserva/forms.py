from django import forms
from apps.reserva.models import Reserva
from apps.reserva.models import ReservaIntermedia
from apps.reserva.models import TipoReserva

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
            'tiempo_estadia': 'Tiempo de estadìa',
            'fecha_salida': 'Fecha de salida',
            'precio_aproximado': 'Precio aproximado',
        }

        widgets = { 
            'perro': forms.Select(attrs={'class':'form-control'}),
            'tipo_reserva': forms.Select(attrs={'class':'form-control'}),
            'fecha_entrada': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_aprox'}),
            'tiempo_estadia': forms.NumberInput(attrs={'class':'form-control','id':'peso','placeholder':'Tiempo de estadìa en dìas'}),
            'fecha_salida': forms.DateInput(attrs={'class':'datepicker form-control', 'id':'epoca_celo_aprox'}),
            'precio_aproximado': forms.NumberInput(attrs={'class':'form-control','id':'peso','placeholder':'Valor a cobrar aproximado'}),
        }


