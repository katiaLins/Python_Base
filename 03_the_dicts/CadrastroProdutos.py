#!/usr/bin/env python3
"""Cadastro de Produtos"""
__version__: "0.1.0"

#Inicio Código
from pprint import pprint 

produto = {
    "nome": "caneta",
    "cores": ["azul", "Branco"],
    "preco": 3.25,
    "dimensao": {
        "altura": 12.1,
        "Largura": 0.8,
    },
    
    "codigo": 45690,
    "codebar": None,
}

cliente = {
    "nome": "Katia"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "qt": 3,
}

total = compra["qt"] * compra["produto"]["preco"]

pprint(f"O cliente {compra['cliente']['nome']} "
      f" comprou {compra['qt']} unidades de {compra['produto']['nome']}" 
      f" e pagou R$ {total}"
)
