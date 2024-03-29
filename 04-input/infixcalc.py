#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[oepração] [n1] [n2]

oepração:
sun -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 4
9

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
oepração : sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`.
"""

__version__ = "0.1.0"

import sys
import os

from datetime import datetime 


while True:

    arguments = sys.argv[1:]
    # Validação
    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
        
    elif len(arguments) != 3:
        print("Número de argumentos invalidos")
        print("Ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)


    validated_nums = []
    for num in nums:
        # TODO: Repetição while + exceptions
        if not num.replace(".", "").isdigit():
            print(f"Número Inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except VAllueError as e:
        print(str(e))
        sys.exit(1)


    # TODO: User dict de funcoes 
    if operation == "sum":
        resultado = n1 + n2

    elif operation == "sub":
        resultado = n1 - n2

    if operation == "mul":
        resultado = n1 * n2

    if operation == "div":
        resultado = n1 / n2

    # path = "/" teste erro de permissão em diretório

    path = os.curdir 
    filepath = os.path.join(path,  "infixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    print(f"O resultado é: {resultado}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} -  {user} - {operation}, {n1 }, {n2} = {resultado}\n")
        # print(f"{operation}, {n1 }, {n2} = {resultado}, file=open(filename, "a"))
    except PermissionError as e:
        # TODO: logging 
        print(str(e))
        sys.exit(1)
    if input("Pressione Enter para continuar, ou qualquer tecla para sair."):
        break


    







