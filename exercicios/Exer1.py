'''
num1 = int(input("informe o nome: "))
num2 = int(input("informe o nome: "))
num3 = num1+num2
print(num3)
var = input("informe o nome: ")
if int(var) > 5:
    print('O número digitado é maior que 5')
elif int(var) < 5:
    print('O número digitado é menor que 5')
else:
    print('O número digitado é 5')
    '''

nome = input("Informe um nome!")
idade = int(input("Informe a idade!"))

if idade >= 18:
    print(nome, 'tem', idade, 'e é maior de idade')
else:
    print(nome, 'tem', idade, 'e não é maior de idade')