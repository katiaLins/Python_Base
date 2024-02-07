#!/usr/bin/env python3

import sys
import logging


ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias":dias
            }

except FileNotFoundError:
    logging.error("Arqivo reservas.txt  não existe")
    sys.exit(1)


quartos= {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), #TODO: Decimal
            "disponivel":False if int(codigo) in ocupados else True
            }

except FileNotFoundError:
    logging.error("Arqivo reservas.txt  não existe")
    sys.exit(1)



print(f"Reserva Hotel Python.")
print(f"-" * 40)
if len(ocupados) == len(quartos):
    print("Não temos mais vagas.")
    sys.exit(1)
    
nome = input("Nome do Cliente: ").strip()


for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "Ocupado" if not dados['disponivel'] else "Livre"
    # TODO: Substituir casa decimal por virgula.
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} -  {disponivel}")
    
print(f"-" * 40)

try:
    num_quarto = int(input("Numero do quarto: ").strip())
    if not quartos[num_quarto] ["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Número Ivalido")
    sys.exit(1)
except KeyError:
    logging.error("O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Quantos dias?: ").strip())
except ValueError:
    logging.error("Número Ivalido")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total =  preco_quarto * dias

#print(f"{nome},{num_quarto},{dias}")
with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")
