from django.db import models

#carousel

class Driver(models.Model):
	"""Model representing a DRIVER."""
	nombre = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	año = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ['nombre', 'modelo']

	def get_absolute_url(self):
		return reverse('Tarjeta-detail', args=[str(self.id)])
		

class Registro(models.Model):	
	nombre =models.CharField(max_length=40, verbose_name="Nombre")
	apellido =models.CharField(max_length=40, verbose_name="Apellido")
	email =models.EmailField(max_length=50, verbose_name="Correo")
	usuario =models.CharField(max_length=40, verbose_name="Usuario")
	contraseña =models.CharField(max_length=40, verbose_name="Contraseña")
	telefono =models.CharField(max_length=10, verbose_name="Telefono")

	def __str__(self):
		return self.nombre


 
