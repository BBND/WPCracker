#!/usr/bin/python2
# coding: utf-8
import json
import sys

import requests

from .wpCracker import print_table

G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'


def enum(wp_url):
    try:
        r = requests.get(wp_url + "/wp-json/wp/v2/users")
    except Exception:
        sys.exit(R + "[!] Invalid URL ! Please add http/https protocol.")
    if 'description' in r.text:
        table = []
        header = ['Id', 'Fullname', 'Username']
        r_json = json.loads(r.text)
        print(R + "[+] " + str(len(r_json)) + " users are found !" + W)
        for i in range(0, len(r_json)):
            enum_id = r_json[i]['id']
            enum_fullname = r_json[i]['name']
            enum_username = r_json[i]['slug']
            table.append([enum_id, enum_fullname, enum_username])
        print(print_table(table, header))
    else:
        flag = True
        i = 0
        table = []
        header = ['Id', 'Username']
        while flag:
            r2 = requests.get(wp_url + "/?author=" + str(i + 1))
            uri = r2.url
            if '/author/' in uri:
                table.append([i + 1, uri.split("/author", 1)[1].replace("/", '').lstrip()])
                i = i + 1
            else:
                flag = False
        print(R + "[+] " + str(i) + " users are found !" + W)
        print(print_table(table, header))
        if i == 0 and not flag:
            print(G + "[+] This url is protected against enumeration attack !")
