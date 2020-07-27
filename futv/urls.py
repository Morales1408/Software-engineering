"""
Este documento sirve para poder leer correctamente las páginas que hemos preestablecido en nuestro archivo "views"

"""
# Librerías predeterminadas para la utlización correcta
from django.contrib import admin
from django.urls import path
# Importo las páginas que haya creado
from futv.views import * 

# Declaro que mi sistema tiene dos posibles vistas para páginas: La página admin (con url /admin/) y la página show (con url /viajes/)
urlpatterns = [
	# Declaro el path primero poniendo la url a la que será acreedora y luego la función (declarada en views) que realizará la acción
    path('admin/', admin.site.urls),
    path('viajes/', show),
]
