#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do some work about cookie"""
import os
import re
import time
from config import COOKIE_DIR
from log import LOGGER

__author__ = 'DESTHUbb'

def is_ip(domain):
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}',domain):
        return True

# get cookie for browser
def get_cookies_list(target_domain):
    if '.' in target_domain:
        cookies_list = []
        # if the domain is IP
        if is_ip(target_domain):
            domain_scope = target_domain
        else:
            # default
            domain_scope = '.' + target_domain.split('.')[-2] + '.' + target_domain.split('.')[-1]
        cookie_file_path = os.path.join(COOKIE_DIR, '_'.join([domain_scope, 'cookie']))
        if os.path.exists(cookie_file_path):
            with open(cookie_file_path, "r")as cookie_file:
                cookie_file_list = cookie_file.readlines()
                expire = cookie_file_list[2]
                # check expire
                if int(time.time()) < int(expire):
                    cookies_text = cookie_file_list[0].strip()
                    domain = cookie_file_list[1].strip()
                    new_list = cookies_text.split(';')
                    for i in new_list:
                        if i != '':
                            cookie_dict = {}
                            key = i.split('=')[0].strip()
                            value = i.split('=')[1].strip()
                            cookie_dict['domain'] = domain
                            cookie_dict['name'] = key
                            cookie_dict['value'] = value
                            cookie_dict['path'] = '/'
                            cookies_list.append(cookie_dict)
        return cookies_list

# save cookie default expire=3600s
def save_cookie(cookie,domain,expire_time=3600):
    domain_scope='.'+domain.split('.')[-2]+'.'+domain.split('.')[-1]
    expire=int(time.time())+expire_time

COOKIE_DIR = "/home/alex/Des-XSS/cookie"

def save_cookie(cookie, domain):
    domain_scope = domain.replace('.', '_')
    cookie_file_path = os.path.join(COOKIE_DIR, f"{domain_scope}_cookie")
    with open(cookie_file_path, 'w+') as cookie_file:
        cookie_file.write(cookie)
        cookie_file.write(cookie + '\n')
        cookie_file.write(domain_scope+'\n')
        cookie_file.write(str(expire))

#  save cookie for http://ip/path
def save_cookie_ip(cookie,ip,expire_time=3600):
    domain_scope=ip
    expire=int(time.time())+expire_time
    with open(os.path.join(COOKIE_DIR,'_'.join([domain_scope,'cookie'])), 'w+')as cookie_file:
        cookie_file.write(cookie + '\n')
        cookie_file.write(domain_scope+'\n')
        cookie_file.write(str(expire))

# get cookie
def get_cookie(target_domain,):
    if '.' in target_domain:
        domain_scope = '.' + target_domain.split('.')[-2] + '.' + target_domain.split('.')[-1]
        cookie_file_path = os.path.join(COOKIE_DIR, '_'.join([domain_scope, 'cookie']))
        if os.path.exists(cookie_file_path):
            with open(cookie_file_path, "r")as cookie_file:
                cookie_file_list = cookie_file.readlines()
                expire = cookie_file_list[2]
                # check expire
                if int(time.time()) < int(expire):
                    cookies_text = cookie_file_list[0].strip()
                    return cookies_text
                else:
                    LOGGER.warn('Cookie of %s is expired!!!' % domain_scope)
        # cookie not exists
        else:
            pass

# get cookie-ip
def get_cookie_ip(ip,):
    domain_scope = ip
    cookie_file_path = os.path.join(COOKIE_DIR, '_'.join([domain_scope, 'cookie']))
    if os.path.exists(cookie_file_path):
        with open(cookie_file_path, "r")as cookie_file:
            cookie_file_list = cookie_file.readlines()
            expire = cookie_file_list[2]
            # check expire
            if int(time.time()) < int(expire):
                cookies_text = cookie_file_list[0].strip()
                return cookies_text
            else:
                LOGGER.warn('Cookie of %s is expired!!!' % domain_scope)
    else:
        pass

def try_cookie(domain):
    # try to find cookie from cookie/ and add it to DEFAULT_HEADER
    cookie = get_cookie(domain)
    if cookie:
        choose = raw_input('\033[1;32m{}\033[0m'.format("Cookie of %s is found in ./cookie/,Do you want to use it? (y/n)"%domain))
        if choose == 'y' or choose == 'yes' or choose=='':
            return cookie

if __name__=='__main__':
    pass


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvement:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do some work about cookies"""

import os
import re
import time
from config import COOKIE_DIR
from log import LOGGER

__author__ = 'DESTHUbb'

def is_ip(domain):
    """Check if the given domain is an IP address."""
    return re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}', domain) is not None

def domain_scope(target_domain):
    """Get the domain scope from the target domain."""
       if is_ip(target_domain):
  return target_domain
    else: 
        return '.'.join(target_domain.split('.')[-2:])

def get_cookie_file_path(scope):
    """Get the cookie file path for the specified domain scope."""
    return os.path.join(COOKIE_DIR, f"{scope}_cookie")

def save_cookie(cookie, domain, expire_time=3600):
    """Save the cookie for the given domain with an optional expiration time (default is 3600 seconds)."""
    scope = domain_scope(domain)
    expire = int(time.time()) + expire_time
    cookie_file_path = get_cookie_file_path(scope)

    with open(cookie_file_path, 'w+') as cookie_file:
        cookie_file.write(cookie + '\n')
        cookie_file.write(scope + '\n')
        cookie_file.write(str(expire))

def get_cookie(target_domain):
    """Get the cookie for the specified target domain if it exists and is not expired."""
    scope = domain_scope(target_domain)

