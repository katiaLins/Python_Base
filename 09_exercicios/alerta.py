#!/usr/bin/ven python3

"""
Alarme temperatura:

"""
import sys
import logging
log = logging.Logger("Alerta")


info = {
    "temperatura": None,
    "umidade": None,    
}
keys = info.keys()


for key in keys:
    try:
        info[key] = float(input(f"Qual {key}: ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} Inválida, tente mais uma vez")
        sys.exit(1)

temp =  info["temperatura"]
umi = info["umidade"]

if temp > 45:
    print("Perigo de calor extremo!!")
elif (temp * 3) >=  umi:
    print("ALERTA!! Perigo de calor umido.")
elif temp >= 10 and temp <= 30:
    print("Temperatura Normal.")
elif temp >= 0 and temp <= 10:
    print("Tempo Frio.")
elif temp < 0:
    print("ALERTA, Frio extremo.")

                
    
    
