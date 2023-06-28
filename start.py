#!/usr/bin/python3.0
# -*- encoding: utf-8 -*-

"""
    @Description: Cli
   
    ~~~~~~
    @Author  : DESTHUbb
    @Time    : 19-10-9  10:13
"""

from gevent import monkey
monkey.patch_ssl()
import urllib.request
import urllib.error



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements made:

1: # I imported the check_url, check_install, save_cookie, save_cookie_ip and is_ip functions directly from their respective modules.

2: # I removed the save_cookie function defined inside the main file, since it is imported from the cookie module.

3: # I replaced cpu_count() with multiprocessing.cpu_count() to get the number of CPU cores.

4: # I changed the id variable to task_id to avoid confusion with the gen_id function.


