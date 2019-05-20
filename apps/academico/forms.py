from django import forms
from .models import *

class InscritoForm(forms.ModelForm):
	class Meta:
		model = Inscrito
		fields = [
			'id',
			'nombres',
			'apellidos',
			'dni',
			'e_mail',
			'telefono',
			'direccion',
			'ugel',
			'observacion',	
		]

		labels = {
			'id':'Código',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'dni' : 'DNI',
			'e_mail': 'Correo Electrónico',
			'telefono' : 'Telefono',
			'direccion':'Direccion',
			'ugel': 'Ugel',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'dni':forms.NumberInput(attrs={'class':'form-control'}),
			'e_mail': forms.EmailInput(attrs={'class':'form-control'}),	
			'telefono':forms.NumberInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'ugel':forms.Select(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
		}

class UgelForm(forms.ModelForm):
	class Meta:
		model = Ugel
		fields = [
			'id',
			'nombre',
			'director',
			'observacion',
		]

		labels = {
			'id':'Codigo',
			'nombre': 'Ugel',
			'director':'Director',
			'observacion': 'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'director':forms.TextInput(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
		}

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = [
			'id',
			'nombre',
			'costo',
			'cant_modulos',
			'observacion',
		]

		labels = {
			'id':'Codigo',
			'nombre': 'Curso',
			'costo':'Costo',
			'cant_modulos': 'Cantidad de Modulos',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'costo':forms.NumberInput(attrs={'class':'form-control'}),
			'cant_modulos': forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.Textarea(attrs={'class':'form-control'}),
		}

class MatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula
		fields = [
			'id',
			'inscrito',
			'curso',
			'modulos_entregados',
			'asesora',
			'beneficiario',
			'fecha_matricula',
			'fecha_diploma',
			'promocion',
			'descuento_actual',
			'descuento_pendiente',
			'observacion',
		]

		labels = {
			'id':'Codigo',
			'inscrito': 'Inscrito',
			'curso':'Curso',
			'modulos_entregados': 'Modulos Entregados',
			'asesora':'Asesora',
			'beneficiario':'Beneficiario',
			'fecha_matricula':'Fecha de Matrícula',
			'fecha_diploma':'Fecha de Entrega de Diploma',
			'promocion':'Promoción',
			'descuento_actual':'Descuento Actual',
			'descuento_pendiente':'Descuento Pendiente',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'inscrito': forms.Select(attrs={'class':'form-control'}),
			'curso':forms.Select(attrs={'class':'form-control'}),
			'modulos_entregados': forms.Textarea(attrs={'class':'form-control'}),
			'asesora':forms.TextInput(attrs={'class':'form-control'}),
			'beneficiario':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_matricula':forms.DateInput(attrs={'class':'form-control'}),
			'fecha_diploma':forms.DateInput(attrs={'class':'form-control'}),
			'promocion':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_actual':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_pendiente':forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.Textarea(attrs={'class':'form-control'}),
		}

