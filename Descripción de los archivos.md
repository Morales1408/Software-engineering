### Carpeta `/apps/base_dato/`
La carpeta con nombre `/apps/` fue creada para albergar a todas las aplicaciones que sirvan como complemento para nuestro proyecto.

En la carpeta `/apps/base_dato/` podemos encontrar los siguientes documentos

|Nombre|Descripción|
|:---|:----|
|__ pycache__|Carpeta creada por defecto en Django que sirve para la utilización de las aplicaciones en el sistema|
|migrations|Contiene el registro de cada una de las migraciones (modificaciones) que se han hecho en la aplicación "base_dato"|
|__ init__.py|Archivo creado por defecto en Django para la utilización de la aplicación "base_dato". No se le hicieron modificaciones|
|admin.py|Aquí se importaron las tablas requeridas de mi base de datos para poder visualizarlas en la página de administración de Django|
|apps.py|Archivo creado por defecto en Djang para el registro de las aplicaciones dependientes de "base_dato". No se le hicieron modificaciones|
|models.py|Aquí se declararon y delimitaron las tablas contenidas en mi base de datos con sus respectivas características|
|test.py|Archivo creado por defecto en Django para garantizar la usabilidad de la aplicación "base_dato". No se le hicieron modificaciones|
|views.py|Archivo creado por defecto en Django para crear views dependientes de la aplicación "base_dato". No se le hicieron modificaciones|
-----------------
### Carpeta `/futv/`

La carpeta con nombre `/futv/` fue creada como repositorio __principal__ del proyecto. 

En la carpeta `/futv/` podemos encontrar los siguientes documentos

|Nombre|Descripción|
|:---|:---|
|__ pycache__|Carpeta creada por defecto en Django que sirve para la utilización y memoria del proyecto en general|
|__ init.py|Archivo creado por defecto en Django para la utilización del proyecto. No se le hicieron modificaciones|
|asgi.py|Archivo por defecto en Django que sirve para la migración del proyecto a producción. No se le hicieron modificaciones|
|settings.py|Archivo creado por defecto en Django para configurar características predeterminadas en los ambientes. Aquí se hizo la conección a la base de datos con postgreSQL y se cambió el idioma a Español. Todo lo demás está por defecto|
|urls.py|Aquí se declaraban las direcciones URL de la páginas previamnete estipuladas en `/futv/views.py`|
|views.py|Aquí se declaraban las páginas que tendría disponible el sistema así como las acciones que realizarían cada una de estas|
|wsgi.py|Archivo creado por defecto en Django que sirve para la migración del proyecto a producción. No se le hicieron modificaciones|
--------------------
### Carpeta `/templates/`

La carpeta con nombre `/templates/` únicamente alberga archivos de formato html que sirven como complemento para la visualización de las páginas declaradas en `/futv/views.py`

En la capeta `/templates/` podemos encontrar el siguiente documento

|Nombre|Descripción|
|:-----|:-------|
|vista.html|Sirvió como complemento a la visualización de la página "viajes" declarada en `/futv/views.py`|

------
### El archivo `/manage.py`

El archivo `/manage.py`es el encargado de orquestar a todos los demás elementos utilizados en el proyecto; basta con ejecutarlo con los requerimientos previos (Django y postgreSQL instalados) para que el proyecto comience a funcionar.



