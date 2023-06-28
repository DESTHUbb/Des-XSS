#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Check if the browser installed correctly.
    
    ~~~~~~ 
    @Author  : DESTHUbb
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvement:

#!/usr/bin/env python3

"""
@Description: Check if the browser is installed correctly and check a given URL.
@Author: [tu nombre aquí]
@Time: [fecha aquí]
"""

import logging
import urllib.request
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_browser_installation():
    try:
        driver = webdriver.Chrome()
        


