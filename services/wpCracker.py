#!/usr/bin/python2
# coding: utf-8

G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'


def banner():
    print("-----------------------------------------------------------------------")
    print(G + "	WP SECURITY SCANNER  " + W + "v1.0 \n")


def menu():
    print("Usage : This tool is a python script used to ...")
    print("------------------------------------------------------------------------\n")
    print('Options : ')
    print(' -e [URL] ,--enum [URL]			Set url for wordpress user enumeration. \n')
    print(' -v [URL] ,--version [URL]		Set url to get WP version. \n')
    print(' -p [URL] ,--plugins [URL]		Set url to get all plugins. \n')
    print('	-h , --help						Show documentation. \n')
    print("------------------------------------------------------------------------\n")


def print_table(iterable, header):
    max_len = [len(x) for x in header]
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        for index, col in enumerate(row):
            if max_len[index] < len(str(col)):
                max_len[index] = len(str(col))

    output = '-' * (sum(max_len) + 1) + '\n'
    output += '|' + ''.join([h + ' ' * (l - len(h)) + '|' for h, l in zip(header, max_len)]) + '\n'
    output += '-' * (sum(max_len) + 1) + '\n'
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        output += '|' + ''.join([str(c) + ' ' * (l - len(str(c))) + '|' for c, l in zip(row, max_len)]) + '\n'

    output += '-' * (sum(max_len) + 1) + '\n'
    return output
