#!/usr/bin/env python3
"""Hello word mult Linguas.

Dependendo da ligua configurada no ambiente o programa exibe mesagem
correspondente.
Como Usar: 

Tenha a várial LANG devidademente configurada.
    export LANG=pt_BR
Ou informar atraves do CLI argument `--lang`
Ou o usuário terá que digitar.

Execução: 
    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
_autor__ = "katia Lins"
__license__ = "Unlicence"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Instacia logging
log = logging.Logger("Logs.py", log_level)
# level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)



arguments = {"lang" : None,"count" : 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use ´=´, You passed %s, try --key=value: %s",
            arg, 
            str(e)
        )
        
        sys.exit(1)  


    
    key = key.lstrip("-").strip()
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Ivalid Options `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language?")

    
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá Mundão!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Mode!",
}

"""
    Caso queira definir uma liguagem padrão e esconder erro a baixo.
    try com valor default
    message = msg.get(current_language, msg["en_US"])
"""
try:
    message = msg[current_language]
except KeyError as e:
    print(str(e))
    print(f"Language is invalid, choose fron: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
