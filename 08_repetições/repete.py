#!/usr/bin/env python3
'''dados = {}
for line in open("post.txt"):
    if line == "---\n":
      break
    key, valor = line.split(":")
    dados[key] = valor.strip()
    
print(dados)
'''
dados = {}

for line in open("post.txt"):
    if ":" in line:
        key, valor, valor1 = line.split(":")
        dados[key] = valor.strip()
print(dados)


# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip() 
    for line in open("post.txt") 
    if ":" in line
}
print(dados)


original = [1,2,3,4,5]

#for loops / larço for
#Abordagemo estruturada

dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

#Abordagemo Funcional
#List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

