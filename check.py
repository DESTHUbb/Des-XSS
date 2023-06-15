#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Check if the browser installed correctly.
    
    ~~~~~~ 
    @Author  : longwenzhang
    @Time    : 19-10-29   3:46
"""
import urllib.request
from log import LOGGER
from selenium import webdriver

def check_install():
    try:
        br = webdriver.Chrome()
    except Exception as e:
        LOGGER.info(e)
        try:
            br = webdriver.PhantomJS()
        except Exception as e:
            LOGGER.info(e)
            LOGGER.warn('No browser is installed correctly!')
        else:
            br.quit()
            LOGGER.info('Phantomjs is installed correctly.')
    else:
        br.quit()
        LOGGER.info('Chrome is installed correctly.')
        try:
            br = webdriver.PhantomJS()
        except Exception as e:
            LOGGER.info(e)
        else:
            br.quit()
            LOGGER.info('Phantomjs is installed correctly.')
    exit(0)

def check_url(url):
    try:
        urllib.request.urlopen(url,timeout=20)
    except Exception as e:
        LOGGER.warn('Check url error: '+str(e))
        exit(0)

        
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

DESCRIPTION:
    
    This is a python script that has two functions: check_install() and check_url(url).

The check_install() function checks if the Chrome or PhantomJS browser is correctly installed on the system.
First, it tries to start an instance of Chrome. If this fails, try starting a PhantomJS instance.
If both attempts fail, the script logs a warning message indicating that neither browser is installed correctly.
If one or both browsers start successfully, the script logs a message indicating that the browsers are installed correctly

The check_url(url) function checks if a given URL is accessible online.
It uses the Python urllib2 library to open the provided URL, and if an error occurs, the script logs a warning message that the URL cannot be accessed.

Also, the script imports two modules: urllib2 and selenium.
    The urllib2 module is used in the check_url() function to access a provided URL, while the selenium module is used in the check_install() function to start a Chrome or PhantomJS instance.
    It also imports a custom module called log, which contains a LOGGER object used to record log messages.
        
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7        
IMPROVED AND UPDATED VERSION: PYTHON3
    
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@Description: Check if the browser is installed and can be launched successfully.

    ~~~~~~
    @Author  : DESTHUbb
    @Time    : 19-10-29   3:46
    """

import logging
import platform
import subprocess
import sys
import urllib.request
from selenium import webdriver


def check_install():
    """
    Check if the browser (Chrome or Firefox) is installed and can be launched successfully.
    """
    try:
        browser = webdriver.Chrome()
    except Exception as e:
        logging.info(e)
        try:
            browser = webdriver.Firefox()
        except Exception as e:
            logging.warning('No browser is installed or can be launched successfully!')
        else:
            browser.quit()
            logging.info('Firefox is installed and can be launched successfully.')
    else:
        browser.quit()
        logging.info('Chrome is installed and can be launched successfully.')
        try:
            browser = webdriver.Firefox()
        except Exception as e:
            logging.info(e)
        else:
            browser.quit()
            logging.info('Firefox is installed and can be launched successfully.')
    sys.exit(0)


def check_url(url):
    """
    Check if the given URL is accessible online.
    """
    try:
        urllib.request.urlopen(url, timeout=20)
    except Exception as e:
        logging.warning(f'Check URL error: {e}')
        sys.exit(0)


def check_os():
    """
    Check if the operating system is supported.
    """
    os = platform.system()
    if os not in ['Windows', 'Linux', 'Darwin']:
        logging.warning(f'The operating system {os} is not supported.')
        sys.exit(0)


def check_dependencies():
    """
    Check if the required dependencies are installed.
    """
    try:
        subprocess.check_output(['which', 'chromedriver'])
        subprocess.check_output(['which', 'geckodriver'])
    except subprocess.CalledProcessError:
        logging.warning('The required dependencies (chromedriver and geckodriver) are not installed.')
        sys.exit(0)


def main():
    check_os()
    check_dependencies()
    check_install()
    check_url('https://example.com')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
Esta versión actualizada del script tiene las siguientes mejoras:

Se ha actualizado la sintaxis de Python para utilizar Python 3.
Se ha mejorado la estructuración y organización del código y añadido funciones adicionales para comprobar el sistema operativo y las dependencias requeridas.
Se ha añadido el control de excepciones y el manejo de errores para proporcionar mensajes de registro más descriptivos y claros.
Se ha actualizado el módulo urllib2 a urllib.request para la comprobación de URL.
La función check_dependencies() comprueba si los controladores del navegador (chromedriver y geckodriver) están instalados en el sistema. 
Si alguno de estos controladores no está instalado, el script registra un mensaje de advertencia indicando que las dependencias requeridas no están instaladas.

La función check_os() comprueba si el sistema operativo en el que se ejecuta el script es Windows, Linux o macOS. 
Si el sistema operativo no está en esta lista, el script registra un mensaje de advertencia indicando que el sistema operativo no es compatible.

La función main() llama a las funciones check_os(), check_dependencies(), check_install() y check_url() para comprobar si el sistema cumple con los requisitos necesarios para ejecutar el script.

La función check_install() comprueba si el navegador Chrome o Firefox están instalados y se pueden iniciar correctamente. 
Si ambos navegadores se inician correctamente, el script registra un mensaje indicando que los navegadores están instalados y se pueden iniciar correctamente.

La función check_url() comprueba si una URL proporcionada es accesible en línea. 
Utiliza la biblioteca urllib.request de Python para abrir la URL proporcionada y, si se produce un error, el script registra un mensaje de advertencia indicando que la URL no se puede acceder.

Además, el script utiliza el módulo logging para registrar mensajes de registro en lugar de utilizar un módulo personalizado.



