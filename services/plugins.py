#!/usr/bin/python2
# coding: utf-8
import re
import sys
import time

import requests

G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'


def get_plugins(wp_url):
    try:
        r = requests.get(wp_url)
    except Exception:
        sys.exit(R + "[!] Invalid URL ! Please add http/https protocol.")

    plugins = re.findall('/wp-content/plugins/(.*?)/.*?ver=([0-9\.]*)', r.text, re.DOTALL)
    unique_plugins = {}

    # Get unique plugins
    for plugin in plugins:
        name = plugin[0]
        version = plugin[1]
        print(name + ' ' + version)
        if name not in unique_plugins.keys():
            unique_plugins[name] = version
    print(R + "[+] " + str(len(unique_plugins)) + " plugins are found !" + W)
    print("PLease wait to list plugins ...")
    time.sleep(3)
    # Print plugins
    for key, value in unique_plugins.items():
        print(W + "| " + key + " version " + value)
