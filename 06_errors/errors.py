#!/usr/bin/env python3
"""
Tratamento de erros em Python.
"""
import os
import sys 

if os.path.exists("names.txt"):
    input("...") # Race Condition
    names = open("names.txt").readlines()
else: 
     print("[Error]: File names.txt not found.")
     sys.exit(1)

# LBYL - Look Before You Leap

if len(names) >= 3:
    print(names[1])
else: 
    print("[Error]: Mising name in the list")
    sys.exit(1)
