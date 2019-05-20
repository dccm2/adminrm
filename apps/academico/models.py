from django.db import models

class Curso(models.Model):
	id = models.AutoField(primary_key= True, null=False)
	nombre = models.CharField(max_length=100, unique=True)
	costo = models.IntegerField()
	cant_modulos = models.IntegerField()
	observacion = models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Ugel(models.Model):
	id= models.AutoField(primary_key= True, null=False)
	nombre = models.CharField(max_length=100,unique=True)
	director = models.CharField(max_length=100, blank=True, null=True)
	observacion = models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']


class Inscrito(models.Model):
	id = models.IntegerField(primary_key = True, unique=True)
	nombres = models.CharField(max_length=70)
	apellidos = models.CharField(max_length=70)
	dni= models.IntegerField(unique=True)
	e_mail= models.EmailField()
	telefono = models.IntegerField()
	direccion = models.CharField(null=True,max_length=150)
	ugel = models.ForeignKey(Ugel, null=True, blank=True, on_delete='CASCADE')
	observacion = models.TextField(max_length=2000, null=True, blank=True)
	

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	class Meta:
		ordering = ['id']

class Matricula(models.Model):
	id = models.AutoField(primary_key= True, null=False)
	inscrito = models.ForeignKey(Inscrito, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	modulos_entregados=models.TextField(max_length=3000, blank=True,null=True)
	asesora = models.CharField(null=True,max_length=50)
	beneficiario = models.CharField(null=True,max_length=100, blank=True)
	fecha_matricula = models.DateField(null=True)
	fecha_diploma = models.DateField(null=True)
	promocion = models.CharField(max_length=200, null=True)
	descuento_actual = models.IntegerField(null=True)
	descuento_pendiente = models.IntegerField(null=True)
	observacion = models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.inscrito)