#!/usr/bin/ven python3

"""
Alarme temperatura:

"""
import sys
import logging
log = logging.Logger("Alerta")

# TODO: Usar funções para ler input


info = {
    "temperatura": None,
    "umidade": None,    
}

while True:
    #condição de parada
    #O dicionario esta completamente preenchido
    info_size = len(info.values()) 
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break
    
    for key in  info.keys(): #[temperatura umidade]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"Qual {key}: ").strip())
        except ValueError:
            log.error("%s invalida, digite Números", key)
            break

    

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

                
    
    
