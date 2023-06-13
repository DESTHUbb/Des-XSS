#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: print logo.
    
    ~~~~~~ 
    @Author  : longwenzhang
    @Time    : 19-10-9  10:28
"""
import os
from config import BASE_DIR

def banner():
    with open(os.path.join(BASE_DIR,'logo'))as banner_f:
        a=banner_f.read()
    BANNER = """\033[01;33m"""+a+"""\033[0m"""
    print BANNER

if __name__=='__main__':
    banner()
    
    
    /////////////////////////////////////
    
    new 
    
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @Description: Script to print a welcome message.
    
    ~~~~~~ 
    @Author  : My Name
    @Time    : 2023-06-13  10:00
"""

def welcome():
    message = "Welcome to my Python script!"
    print(message)

if __name__ == '__main__':
    welcome()
