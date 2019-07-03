#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 06:17:37 2019

@author: skyking
"""

import time
from datetime import datetime as dt

hosts_temp = "hosts copy.txt"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
        print("Working Hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("Fun hours")
    
    time.sleep(5)