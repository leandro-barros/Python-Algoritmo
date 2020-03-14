num = float(input('Informe um número real!'))
x = 0

for i in range(0, 200):
    if i % 10 == 0:
        print(' ')
    print(i+1, ' = ', num*(i+1))