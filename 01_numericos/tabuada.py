#!/usr/bin/env python3
""" Programa para imprimir tabudade de 1 ao 10.""" 
__version__ = "0.1.1"
__autor__ = "Katia"


#Inicio do código

#base = [1,2,3,4,5,6,7,8,9,10]
#Iterable = Obejtos percorriveis 
numeros = list(range(1,11))

# para casa nuero em nurmeros
for n1 in numeros :
   print("{:-^18}".format(f"Tabuada do {n1}"))
   print()
   for n2 in numeros :
        resultado = n1 * n2 
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
   print("#" * 18)
        
        
         

     
