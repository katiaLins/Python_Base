#!/usr/bin/env python3
"""
Tratamento de erros em Python.
"""
import os
import sys 

# Abordagem de tratamento de erros recomendada, pythônica!
# EAFP - Easy to ASK Forgiveness tha permission
#       (É mais facil pedir perdão do que permissão)

"""
try:
    raise RuntimeErro("Ocoorreu um erro") # Apresenta um erro por conta própia.
except Exception as e:
    print(str(e))
    
"""

    
try:# tradução de try: " tente"
    names = open("names.txt").readlines()
except FileNotFoundError as e: # as e = captura de erro 
     print(f"{str(e)}.")
     sys.exit(1)
     # TODO: Usar retry
finally: # Vai ser executado independente do erros 
    print("Execute isso sempre")
try:
    print(names[8])
except: # Bare excep, ignora qalquer tipo de erro.
    print("[Error]: Mising name in the list")
    sys.exit(1)
