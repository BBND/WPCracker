#!/usr/bin/python2
# coding: utf-8
import argparse
import os

from services.enum import enum
from services.plugins import get_plugins
from services.version import get_version
from services.wpCracker import banner
from services.wpCracker import menu

if __name__ == '__main__':
	os.system("clear")
	banner()
	menu()

	parsing = argparse.ArgumentParser(description="This tool is a python script used to get ...")

	parsing.add_argument('-e', '--enum', dest='enum', help='Set url for wordpress user enumeration.')
	parsing.add_argument('-v', '--version', dest='version', help='Set url to get wordpress version')
	parsing.add_argument('-p', '--plugins', dest='plugin', help='Set url to get all wordpress plugins')
	args = parsing.parse_args()
	
	url_enum = args.enum
	url_version = args.version
	url_plugin = args.plugin

	if url_enum is not None:
		enum(url_enum)
	elif url_version is not None:
		get_version(url_version)
	elif url_plugin is not None:
		get_plugins(url_plugin)	
	else :
		pass

