#!/usr/bin/env python3
"""
Bloco de notas terminal.
$ notes.py new "Minha Nota" 
tag: Tech
text: 
Anotação geral sobre tecnologia.

$ notes.y read tag

...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path  = os.curdir 
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must spucify subcommand: {cmds}")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)
    
if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    # criação das notas
    title = arguments[1] # TODO: testar exception
    text = [
        f"{title}", 
        input("tag:").strip(),
        input("text:\n").strip(),
        
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
