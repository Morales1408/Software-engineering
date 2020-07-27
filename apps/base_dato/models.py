'''
Esta parte del código es referente a los modelos, los modelos en este caso son las tablas que existen en mi base de datos. 
Cada clase referente a una tabla en mi base de datos. 
'''

from django.db import models
# Create your models here.

# Creo mi tabla "choferes" con las columnas  nombre, fecha de contrato, y edad. 
class chofere(models.Model):
	# Declaro la columna nombre como el primary key de esta tabla
	nombre = models.CharField(max_length=30,verbose_name='Nombre del chofer',primary_key=True,default='Ninungo')
	fecha_contrato = models.DateField(verbose_name='Fecha de contrato')
	edad = models.IntegerField(verbose_name='Edad del conductor')

# Creo mi tabla "unidade" con las columnas  número de unidad, fecha de adquisicion, chofer. 
class unidade(models.Model):
	# Declaro la columna numero como el primary key de esta tabla
	numero = models.CharField(max_length=30,verbose_name='Número de la unidad',primary_key=True,default='Unidad')
	fecha_adquisicion = models.DateField(verbose_name = 'Fecha de adquisición')
	# Declaro la columna chofer como una tabla relacional tipo Many To Many que redirige a la tabla chofere
	chofer = models.ManyToManyField(chofere,verbose_name='Nombre del conductor designado')


# Creo mi tabla "usuario" con las columnas   nombre, fecha, boletos, hora, unidad.
class usuario (models.Model):
	# Declaro la columna nombre como el primary key de esta tabla
	nombre = models.CharField(max_length=30,verbose_name='Nombre del usuario',primary_key=True,default=1)
	fecha = models.DateField(verbose_name = 'Fecha en que viaja')
	boletos = models.IntegerField( verbose_name='Boletos que compró')
	hora = models.CharField(max_length=30,verbose_name='Hora a la que viaja')
	# Declaro la columna unidad como una tabla relacional tipo Many To Many que redirige a la tabla unidade
	unidad = models.ManyToManyField(unidade,verbose_name='Unidad en la que viaja')


# Creo mi tabla "viaje"  con las columnas  número de unidad, duración de viaje, fecha, precio de viaje, paradero y destino. 
class viaje(models.Model):
	# Declaro la columna numero_unidad como una tabla relacional tipo Many To Many que redirige a la tabla unidade
	numero_unidad = models.ManyToManyField(unidade, verbose_name= 'Número de la unidad')
	duracion_viaje = models.IntegerField(verbose_name='Duración aproximada del viaje (hrs)')
	fecha = models.DateField()
	precio_viaje = models.FloatField(verbose_name ='Precio del boleto')
	asientos = models.IntegerField(verbose_name='Asientos disponibles')
	hora = models.CharField(max_length=30, verbose_name='Hora a la que sale el viaje')
	paradero = models.CharField(max_length=30, verbose_name='Punto de partida',default = 'Paradero')
	destino = models.CharField(max_length=30,verbose_name='Destino final',default = 'Destino')
