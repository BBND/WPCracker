#!/usr/bin/python2
# coding: utf-8
import json
import re
import sys
import time

import requests

G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'

def get_version(wp_url):
	try:
		r = requests.get(wp_url)
	except Exception:
		sys.exit(R + "[!] Invalid URL ! Please add http/https protocol.")

	version = re.search(r'content="WordPress ([0-9]+\.[0-9]+\.?[0-9]*)',r.text)
	if version :
		print(R + "[!!] This website use the version " + version.group(1))
		print(W + "Checking if this version is vulnerable ...")
		time.sleep(3) 
		rv = requests.get("https://wpvulndb.com/api/v2/wordpresses/"+version.group(1).replace('.',''))
		json_v = json.loads(rv.text)
		table = []
		header = ['Title', 'Published date', 'References', 'CVE', 'Type']
		for j,v in json_v.items() :
			if v["vulnerabilities"] != [] :
				for vulne in v["vulnerabilities"] :
					title = vulne["title"]
					published = re.search(r'([0-9]+\-[0-9]+\-.?[0-9]*)T' , vulne["published_date"])
					references = '\n'.join(vulne["references"]["url"])
					cve = vulne["references"]["cve"][0]
					type_v = vulne["vuln_type"]
					print(W+'-------------------------------------------------------------')	
					print(R + title + '\n' + Y + 'Published : ' + published.group(1) + '\n' + references + '\n' + 'CVE : ' + cve + '\n' + 'type : ' + type_v + '\n')
					print(W+'-------------------------------------------------------------')
			else :
				print(G + "[+] This version is not vulnerable ")

	else :
		print(G + "[+] Cannot found WP version.")
