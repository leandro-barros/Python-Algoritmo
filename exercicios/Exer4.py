nome = input('Informe o nome do aluno!')
nota1 = int(input('Informe a nota da prova 1!'))
nota2 = int(input('Informe a nota da prova 2!'))
media = ((nota1 * 2) + (nota2 * 3)) / 5

if media >= 7:
    print('O aluno ',nome,' obteve a média ', media,' e está Aprovado')
elif media < 3:
    print('O aluno ', nome, ' obteve a média ', media, ' e está Reprovado')
else:
    print('O aluno ', nome, ' obteve a média ', media, ' e está de Recuperação')