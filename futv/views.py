'''
Esta archivo llamado views.py contiene cada una de las páginas disponibles en mi sistema. Es decir, si yo tuviera la página
"home", aquí habría una funcion llamada "home". 

'''

#Librerías que me van a servir para la visualización en cada una de mis URLS
from django.http import HttpResponse
# Aquí importo mi base de datos
from apps.base_dato.models import *
from django.template import Template, Context 

#Esta es mi función en donde hago una consulta a mi base de datos para poder mostrarle al usuario los viajes
def show(request):
	f = []
	# Aplico un query SQL sobre mi base de datos para poder extraer todos los viajes disponibkes ahí. 
	for element in viaje.objects.raw('SELECT * FROM base_dato_viaje'):
		#Guardo mis consultas en una lista 
		f.append(element)
	# Abro mi template html
	doc_externo = open('C:/Users/Asus/Desktop/mayra/futv/templates/vista.html')
	# Renderizo mi template
	plt = Template(doc_externo.read())
	# Cierro el template
	doc_externo.close()
	# Aplico el conexto que se enviará al template html para una correcta visualización de la base de datos
	ctx = Context({'Viajes':f})
	# Renderizo mi contexto
	documento = plt.render(ctx) 
	#Consulto mi base de datos

	return HttpResponse(documento)