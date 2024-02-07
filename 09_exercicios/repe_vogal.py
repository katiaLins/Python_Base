#!/usr/bin/env python3
"""

"""
words =[]
while True:
    word = input("Digite uma palavra, | ou Enter para sair:").strip()
    if not word:
        break
        
    final_word = ""
    for letter in word:
       # TODO: remover acentuação usando Função
        if letter.lower() in "aeiouáéóíúãẽĩõũ":
            final_word += letter * 2
        else:
              final_word += letter
    
    # IF ternario
    # final_word += letter * 2 if letter.lower() in "aeiouáéóíúãẽĩõũ"  else  letter

    words.append(final_word)

print(*words, sep="\n")

    
