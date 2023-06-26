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

# Save 'multipart/form-data; boundary=' requests
MULTIPART = []

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements made:

1: # I have added the character encoding at the beginning of the file to avoid problems with special characters.

2: # I've changed the call to os.path.realpath(__file__) to os.path.abspath(__file___) to get the absolute path of the current file more efficiently.

3: # I've changed the call to os.path.join() so that directories are concatenated correctly in Python 3.
