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
import argparse
from multiprocessing import cpu_count
from banner import banner
from engine import Engine
from util import save, gen_id, get_domain_from_url

if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="start.py",description='scan xss from url or file.',usage='start.py --url=url --save')
    parser.add_argument('-v','--version', action='version', version='V1.0-beta')
    parser.add_argument('--check', action='store_true', help='check if browser is installed correctly.')
    parser.add_argument('--url','-u',help='the target site of scan.')
    parser.add_argument('--id',action='store',help='rescan by task id.')
    parser.add_argument('-f','--file',help='scan urls from text file.')
    parser.add_argument('--burp', help='scan from *.xml from burpsuite proxy.')
    parser.add_argument('--process',type=int,help='process number.')
    parser.add_argument('-c','--coroutine',type=int,help='coroutine number.')
    parser.add_argument('--cookie',action='store',help='use cookie.')
    parser.add_argument('--filter', action='store_true', help='filter urls when use --file.')
    parser.add_argument('--clear',action='store_true',help='delete traffic files after scan.')
    parser.add_argument('--browser',action='store',help='scan with browser,is good at Dom-based xss but slow.')
    parser.add_argument('--save',action='store_true',help='save result to json file.')
    banner()
    args=parser.parse_args()
    if args.check:
        from check import check_install
        check_install()
    # default
    url, file, burp = '', '', ''
    filter = False
    # default use number of cpu-core as processes
    num = cpu_count()
    # default
    coroutine = 200
    if args.url:
        from check import check_url
        url = args.url
        num = 1
        check_url(url)
    if args.file:
        file = args.file
    if args.burp:
        burp = args.burp
    if args.filter:
        filter = args.filter
    browser = ''
    if args.browser:
        browser = args.browser
        # default 2 if use browser
        num = 2
        if args.url:
            num = 1
    if args.process:
        num = args.process
    if args.coroutine:
        coroutine = args.coroutine
    if args.cookie:
        from cookie import save_cookie_ip, is_ip
        if file:
            with open(file) as f:
                scope_url = f.readline().strip()
        elif url:
            scope_url = url
        scope_url = "https://example.com/path"
        domain = get_domain_from_url(scope_url)
        if is_ip(scope_url):
            save_cookie_ip(args.cookie, domain)
        else:
            from cookie import save_cookie
    def save_cookie(cookie, domain):
    # Código para guardar la cookie
    # ...

    # Define la variable "cookie" y la variable "domain"
        cookie = "cookie_value"
        domain = "example.com"

# Llama a la función "save_cookie()" pasando las variables "cookie" y "domain" como argumentos
        save_cookie(cookie, domain)
    if url or file or burp or args.id or args.filter:
        if args.id:
            id = args.id
            if not Engine.is_scanned(id):
                LOGGER.error('Task %s not found, exit.' % id)
                exit(0)
        else:
            id = gen_id()
        queue = Queue()
        result_queue = Queue()
        target = "example.com"

        engine = Engine(queue, result_queue, target, id=id, url=url, file=file, burp=burp, process=num, browser=browser, coroutine=coroutine, filter=filter)
        try:
             result = engine.start()
        except KeyboardInterrupt as e:
            LOGGER.info(e)
        else:
            if result:
                save(result, id)
            else:
                LOGGER.info('No xss found!')
            if args.clear:
                from util import clear

                clear(id)
    else:
        LOGGER.error('error: missing a mandatory option (--url, --file, --burp, --id)!')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements made;

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
from check import check_url, check_install
from cookie import save_cookie, save_cookie_ip, is_ip


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="start.py", description='scan xss from url or file.', usage='start.py --url=url --save')
    parser.add_argument('-v', '--version', action='version', version='V2.0-beta')
    parser.add_argument('--check', action='store_true', help='check if browser is installed correctly.')
    parser.add_argument('--url', '-u', help='the target site of scan.')
    parser.add_argument('--id', action='store', help='rescan by task id.')
    parser.add_argument('-f', '--file', help='scan urls from text file.')
    parser.add_argument('--burp', help='scan from *.xml from burpsuite proxy.')
    parser.add_argument('--process', type=int, help='process number.')
    parser.add_argument('-c', '--coroutine', type=int, help='coroutine number.')
    parser.add_argument('--cookie', action='store', help='use cookie.')
    parser.add_argument('--filter', action='store_true', help='filter urls when use --file.')
    parser.add_argument('--clear', action='store_true', help='delete traffic files after scan.')
    parser.add_argument('--browser', action='store', help='scan with browser, is good at DOM-based xss but slow.')
    parser.add_argument('--save', action='store_true', help='save result to json file.')
    banner()
    args = parser.parse_args()

    if args.check:
        check_install()
        
    url, file, burp = '', '', ''
    filter = False
    num = multiprocessing.cpu_count()
    coroutine = 200 
    
    if args.url:
    url = args.url
    num = 1
    check_url(url)

    if args.file:
    file = args.file

    if args.burp:
    burp = args.burp

    if args.filter:
    filter = args.filter

    browser = ''
    if args.browser:
    browser = args.browser
        num = 2
    if args.url:
         num = 1
        
   if args.process:
       num = args.process

   if args.coroutine:
        coroutine = args.coroutine

   if args.cookie:
     if file:
         with open(file) as f:
                scope_url = f.readline().strip()
       elif url:
            scope_url = url

        domain = get_domain_from_url(scope_url)
        if is_ip(scope_url):
            save_cookie_ip(args.cookie, domain)
        else:
            save_cookie(args.cookie, domain)

    if url or file or burp or args.id or args.filter:
        if args.id:
           task_id = args.id
           if not Engine.is_scanned(task_id):
              LOGGER.error('Task %s not found, exit.' % task_id)
              exit(0)
        else:
          task_id = gen_id()

        queue = Queue()
        result_queue = Queue()
        target = "example.com"

        engine = Engine(queue, result_queue, target, id=task_id, url=url, file=file, burp=burp, process=num, browser=browser, coroutine=coroutine, filter=filter)

        try:
            result = engine.start()
          except KeyboardInterrupt as e:
            LOGGER.info(e)
          else:





