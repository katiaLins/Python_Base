#!/user/bin/env python3

"""Imrime a mesagem de um email
Não mande span!!
"""

__version__ = "0.1.1"


import sys
import os


arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo: ")
    sys.exit(1)
filename =  arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)
clientes = []
for line in open(filepath):
  
    name, email = line.split(",")

    # TODO: Substitui por envio de email
    print(f"Enviando email para: {email}")
    print()
    print (
            open(templatepath).read()
            % {
                 "nome": name,
                 "produto": "Creme",
                 "texto": "Produto rejuvenecedor para sua péle.",
                 "link": "www.peledelicia.com.br",
                 "quantidade": 2,
                 "preco": 28.90,
                 "email": email,
                    
                 }
        )
    print("-" * 50)
