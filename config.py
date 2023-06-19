#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Configuration of Des-XSS.
    
    ~~~~~~ 
    @Author  : DESTHUbb
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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#python3 improvement

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration of Des-XSS.
"""

import os

# Global directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COOKIE_DIR = os.path.join(BASE_DIR, 'cookie')
RESULT_DIR = os.path.join(BASE_DIR, 'result')
TRAFFIC_DIR = os.path.join(BASE_DIR, 'traffic')

# Save request errors in the following format:
# [(func_name, request, exception)]
REQUEST_ERROR = []

# Save redirect requests
REDIRECT = []

