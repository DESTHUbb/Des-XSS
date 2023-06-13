#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Check if the browser installed correctly.
    
    ~~~~~~ 
    @Author  : longwenzhang
    @Time    : 19-10-29   3:46
"""
import urllib2
from log import LOGGER
from selenium import webdriver

def check_install():
    try:
        br=webdriver.Chrome()
    except Exception, e:
        LOGGER.info(e)
        try:
            br=webdriver.PhantomJS()
        except Exception, e:
            LOGGER.info(e)
            LOGGER.warn('No browser is installed correctly!')
        else:
            br.quit()
            LOGGER.info('Phantomjs is installed correctly.')
    else:
        br.quit()
        LOGGER.info('Chrome is installed correctly.')
        try:
            br=webdriver.PhantomJS()
        except Exception, e:
            LOGGER.info(e)
        else:
            br.quit()
            LOGGER.info('Phantomjs is installed correctly.')
    exit(0)

def check_url(url):
    try:
        urllib2.urlopen(url,timeout=20)
    except Exception,e:
        LOGGER.warn('Check url error: '+str(e))
        exit(0)
        
        
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7

DESCRIPCION:
    
    Este es un script de Python que tiene dos funciones: check_install() y check_url(url).

La función check_install() comprueba si el navegador Chrome o PhantomJS están instalados correctamente en el sistema. 
En primer lugar, intenta iniciar una instancia de Chrome. Si esto falla, intenta iniciar una instancia de PhantomJS. 
Si ambos intentos fallan, el script registra un mensaje de advertencia indicando que ningún navegador está instalado correctamente. 
Si uno o ambos navegadores se inician correctamente, el script registra un mensaje indicando que los navegadores están instalados correctamente.

La función check_url(url) comprueba si una URL proporcionada es accesible en línea. 
Utiliza la biblioteca urllib2 de Python para abrir la URL proporcionada y, si se produce un error, el script registra un mensaje de advertencia indicando que la URL no se puede acceder.

Además, el script importa dos módulos: urllib2 y selenium. 
    El módulo urllib2 se utiliza en la función check_url() para acceder a una URL proporcionada, mientras que el módulo selenium se utiliza en la función check_install() para iniciar una instancia de Chrome o PhantomJS.
    También importa un módulo personalizado llamado log, que contiene un objeto LOGGER utilizado para registrar mensajes de registro.
        
        
