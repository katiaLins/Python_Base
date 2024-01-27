#!/usr/bin/env python3
""" Exibe relatório das crianças por atividade

    Imprimir a lista de crianças agrupadas por
    sala que frequentam casa uma das atividades.
    
"""
__Version__ = "0.1.1"
##Inicio do código


#Dados
sala1 = ["Bia", "Neto", "Clara", "Heitor", "Marina", "joao"]
sala2 =  ["Nando", "Laura", "Atila", "Geovania", "Lila"]

aula_ingles = ["Bia", "Neto", "Atila","Lila","Nando", "joao"]
aula_musica = ["Bia","Geovania","clara"]
aula_danca = ["Neto","Heitor","Marina","joao", "Nando"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

#Listar alunos em casa atividade por sala.

for nome_at, atividade in atividades:
    print(f"Alunos da atividade {nome_at}\n")
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)
    

    print("Sala 01: ", atividade_sala1)
    print("Sala 02: ", atividade_sala2)
    print("-" * 45)
