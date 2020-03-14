media = 0
soma = 0
positivo = 0
negativo = 0
ppositivos = 0
pnegativos = 0
n = int(input('informe a quantidade de números.'))
for i in range(0,n):
    num = float(input('informe um numero.'))
    if num < 0:
        negativo += 1
    else:
        positivo += 1
    soma += num
media = soma / n
ppositivos = (positivo*100)/n
pnegativos = (negativo*100)/n
print('Média: ',media)
print('Quantidade números positivos: ',positivo)
print('Quantidade números negativos: ',negativo)
print('Percentual números positivos: ',ppositivos)
print('Percentual números negativos: ',pnegativos)