import math

print('Equação do 2º grau')

valorA = int(input('Informe  o valor de A!'))
valorB = int(input('Informe  o valor de B!'))
valorC = int(input('Informe  o valor de C!'))

valorDelta = ((valorB ** 2) - (4 * valorA * valorC))
print('O valor de DELTA é: ', valorDelta)

if valorDelta < 0:
    print('Raízes Imaginárias')
elif valorDelta == 0:
    valorX = (-valorB / (2 * valorA))
    print('Valor de X é: ', valorX)
else:
    valorX = ((-valorB + math.sqrt(valorDelta)) / (2 * valorA))
    valorX2 = ((-valorB - math.sqrt(valorDelta)) / (2 * valorA))
    print('Valor de X1 é: ', valorX)
    print('Valor de X2 é: ', valorX2)