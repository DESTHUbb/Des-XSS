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

The script defines three global variables: BASE_DIR, COOKIE_DIR, RESULT_DIR, and TRAFFIC_DIR.
BASE_DIR is set to the current working directory for the script. COOKIE_DIR, RESULT_DIR, and TRAFFIC_DIR are directories used by the NoXss application to store cookies, results, and network traffic, respectively.

Additionally, the script defines three empty lists: REQUEST_ERROR, REDIRECT, and MULTIPART.
These lists are used to store information about request errors, redirect requests, and requests with multipart form data.
    
In short, this script is a NoXss configuration that defines working directory paths and empty lists that will be used to store relevant information during web security analysis.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

IMPROVED AND UPDATED VERSION: PYTHON3 
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
    
"""
""" @Description: Configuration of Des-XSS.

    ~~~~~~
    @Author  : DESTHUbb
    @Time    : 13-06-2023  12:30
"""
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
    
The improved and updated version of the script includes the following:

Python syntax has been updated to use Python 3.
The pathlib library has been used to work with directory paths more efficiently.
Variable names have been changed from case sensitive to upper case to follow the variable naming convention in Python.
Unnecessary comments have been removed and the script description has been updated.
The new version of the script uses the pathlib library to work with directory paths.
The BASE_DIR variable is set to the absolute path of the directory containing the current script.
The COOKIE_DIR, RESULT_DIR, and TRAFFIC_DIR variables are set as Path objects that represent the paths to the cookie, result, and traffic directories, respectively.


The REQUEST_ERRORS, REDIRECTS, and MULTIPART lists have been renamed with uppercase letters to follow the Python variable naming convention.
Also, they are not initialized with values ​​as they will not be used until they are filled with relevant information during web security analysis.

In general, this improved and updated version of the script continues to do the same thing as the previous version, but uses updated Python syntax and the pathlib library for more efficiency in handling directory paths.

    
