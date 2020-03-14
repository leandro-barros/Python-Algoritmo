maior = 0

for i in range(0, 5):
    altura = float(input('Informe uma altura.'))
    if altura > maior:
        if maior == 0:
            menor = altura
        maior = altura
    elif altura < menor:
        menor = altura
print('Menor altura: ',menor)
print('Maior altura: ',maior)