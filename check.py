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
        driver.quit()
        logging.info('Chrome is installed correctly.')
    except Exception as e:
        logging.warning(f'Chrome is not installed correctly: {str(e)}')
        try:
            driver = webdriver.Firefox()
            driver.quit()
            logging.info('Firefox is installed correctly.')
        except Exception as e:
            logging.warning(f'Firefox is not installed correctly: {str(e)}')
            try:
                driver = webdriver.Edge()
                driver.quit()
                logging.info('Edge is installed correctly.')
            except Exception as e:
                logging.warning(f'Edge is not installed correctly: {str(e)}')
                try:
                    driver = webdriver.Safari()
                    driver.quit()
                    logging.info('Safari is installed correctly.')
                except Exception as e:
                    logging.warning(f'Safari is not installed correctly: {str(e)}')
                    logging.error('No browser is installed correctly!')
                    exit(1)

def check_url(url):
    try:
        urllib.request.urlopen(url, timeout=20)
        logging.info(f'{url} is reachable.')
    except Exception as e:
        logging.warning(f'Check URL error: {str(e)}')
        exit(1)

if __name__ == '__main__':
    check_browser_installation()
    check_url('https://www.google.com/')
A continuación te presento algunas de las mejoras que hice al código:

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements and updates made:

1: # I added a __name__ == '__main__' declaration so that the code inside it is only executed when this module is called directly.

2: # I used the logging library instead of a custom implementation. The logging library is more flexible and offers more options for controlling the output stream of logs.

3: # Modified the check_install() function so that it tests multiple browsers instead of just Chrome and PhantomJS. Also, I added an exception for each browser so the code doesn't stop if a browser installation fails.



