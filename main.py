#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Openfoodfact

the purpose of this script is to use the openfoodfact API 
in order to retrieve data from a list of desired food and find 
a substitute for it

Script Python 3.8
files : main.py, database.py, api.py, load.py, menu.py, Readme.md
"""
import menu

menu = menu.Menu()

if __name__ == '__main__':
    menu.main_menu()