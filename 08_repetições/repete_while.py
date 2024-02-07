#!/use/bin/venv python3

# While - Enquanto
'''
n = 101
i = 0 

while i < n: # condição de parada
    if i == 40:
        break
    print(i)
    i += 1
'''
i = 0
while i < 101: # condição de parada
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
    
