#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Configuration of Des-XSS.
    
    ~~~~~~ 
    @Author  : longwenzhang
    @Time    : 19-10-9  10:16
"""
import os

# global dir
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
COOKIE_DIR = os.path.join(BASE_DIR, 'cookie')
RESULT_DIR = os.path.join(BASE_DIR, 'result')
TRAFFIC_DIR =os.path.join(BASE_DIR, 'traffic')

# save request error
# [(func_name,request,exception),]
REQUEST_ERROR=[]

# save redirect request
REDIRECT=[]

# save 'multipart/form-data; boundary=' request
MULTIPART=[]


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

DESCRIPTION:
    
This is a python script used to configure the NoXss application.
The NoXss application is a web security analysis tool used to protect web applications against malicious code injection attacks, such as XSS (Cross-Site Scripting) attacks.

El script define tres variables globales: BASE_DIR, COOKIE_DIR, RESULT_DIR y TRAFFIC_DIR. 
BASE_DIR se establece como el directorio de trabajo actual para el script. COOKIE_DIR, RESULT_DIR y TRAFFIC_DIR son directorios utilizados por la aplicación NoXss para almacenar cookies, resultados y tráfico de red, respectivamente.

Además, el script define tres listas vacías: REQUEST_ERROR, REDIRECT y MULTIPART. 
Estas listas se utilizan para almacenar información sobre errores de solicitud, solicitudes de redireccionamiento y solicitudes con datos de formulario multipart.

En resumen, este script es una configuración de NoXss que define las rutas de los directorios de trabajo y las listas vacías que se utilizarán para almacenar información relevante durante el análisis de seguridad web.
    
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

VERSION MEJORAD Y ACTUALIZADA:
    #!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
    @Description: Configuration of Des-XSS.

    ~~~~~~
    @Author  : DESTHUbb
    @Time    : 13-06-2023  10:16
"""
import os
from pathlib import Path

# Global directories
BASE_DIR = Path(__file__).resolve().parent
COOKIE_DIR = BASE_DIR / 'cookie'
RESULT_DIR = BASE_DIR / 'result'
TRAFFIC_DIR = BASE_DIR / 'traffic'

# Save request errors
REQUEST_ERRORS = []

# Save redirect requests
REDIRECTS = []

# Save 'multipart/form-data; boundary=' requests
MULTIPART = []
    
  La versión mejorada y actualizada del script incluye lo siguiente:

Se ha actualizado la sintaxis de Python para utilizar Python 3.
Se ha utilizado la biblioteca pathlib para trabajar con rutas de directorios de manera más eficiente.
Se han cambiado los nombres de las variables en mayúsculas y minúsculas a mayúsculas para seguir la convención de nombres de variables en Python.
Se han eliminado los comentarios innecesarios y se ha actualizado la descripción del script.
La nueva versión del script utiliza la biblioteca pathlib para trabajar con rutas de directorios. 
La variable BASE_DIR se establece como la ruta absoluta del directorio que contiene el script actual. 
Las variables COOKIE_DIR, RESULT_DIR y TRAFFIC_DIR se establecen como objetos Path que representan las rutas a los directorios de cookies, resultados y tráfico, respectivamente.

Las listas REQUEST_ERRORS, REDIRECTS y MULTIPART se han renombrado con letras mayúsculas para seguir la convención de nombres de variables en Python. 
Además, no se inicializan con valores ya que no se utilizarán hasta que se llenen con información relevante durante el análisis de seguridad web.

En general, esta versión mejorada y actualizada del script sigue cumpliendo la misma función que la versión anterior, pero utiliza la sintaxis actualizada de Python y la biblioteca pathlib para una mayor eficiencia en el manejo de rutas de directorios.  


    
