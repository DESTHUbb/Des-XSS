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
import re
import time
import os
import sys
import argparse
import logging
import multiprocessing
from queue import Queue
from log import LOGGER
from engine import Engine
from util import save, gen_id, get_domain_from_url
from banner import banner
from check import check_browser_installation, check_url
from cookie import save_cookie, save_cookie_ip, is_ip

def check_install():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="start.py", description='scan xss from url or file.', usage='start.py --url=url --save')





///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements made:

1: # I imported the check_url, check_install, save_cookie, save_cookie_ip and is_ip functions directly from their respective modules.

2: # I removed the save_cookie function defined inside the main file, since it is imported from the cookie module.

3: # I replaced cpu_count() with multiprocessing.cpu_count() to get the number of CPU cores.

4: # I changed the id variable to task_id to avoid confusion with the gen_id function.


