#!/usb/bin/env python3
"""
Programa que imprime números pares

"""
par = []
impar = []
num = 0
for num in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)


