"""
Este documento está relacionado a lo que aparece en la página "admin" de Django. 

"""
# Importo las librerías correspondientes
from django.contrib import admin
# Importo mi base de datos
from apps.base_dato.models import *


# Elijo que se puedan ver la tabla Viaje en la página de adminstración
class Viaje(admin.ModelAdmin):
	# Específicamente, elijo que se puedan ver las columnas fecha, precio, hora, asientos, paradero, destino
	list_display = ("fecha",'precio_viaje','hora','asientos','paradero','destino')
	# Especifico que se puedan realizar búsquedas en la tabla Viaje con base en la fecha y el precio de viaje 
	search_fields = ("fecha","precio_viaje")

# Elijo que se pueda ver la tabla de Chofere en la página de administración
class Choferes(admin.ModelAdmin):
	# Específicamente, elijo que se puedan ver las columnas de nombre, edad, y fecha de contrato.
	list_display = ('nombre','edad','fecha_contrato')
	# Especifico que se puedan realizar búsquedas enl a tabla Chofere con base en el nombre y la edad
	search_fields = ('nombre','edad')

# Elijo que se pueda ver la tabla de Unidades
class Unidades(admin.ModelAdmin):
	# Específicamente, elijo que se puedan ver las columnas de número y fecha de adquisición
	list_display = ('numero','fecha_adquisicion')

# Elijo que se pueda ver la tabla de Usuarios 
class Usuarios(admin.ModelAdmin):
	# Específicamente, elijo que se puedan ver las columnas de nombre, fecha, boletos y hora
	list_display = ('nombre','fecha','boletos','hora')
	# Especifico que se puedan realizar búsquedas en la tabla Usuarios con base en el nombre y la hora
	search_fields = ('nombre','hora')


# Registro mis clases para que ya puedan ser renderizadas por la página de administración.
# Las que aparecen registradas son las que se podrán ver. 
admin.site.register(viaje,Viaje)
admin.site.register(chofere,Choferes)
admin.site.register(unidade,Unidades)
admin.site.register(usuario,Usuarios)