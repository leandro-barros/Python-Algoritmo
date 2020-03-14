valorCompra = int(input('Informe o valor da compra!'))
formaPagamento = input('Informe a forma de pagamento!\n V - Á Vista \n P - Á Prazo\n')

if formaPagamento == 'V':
    desconto = ((valorCompra * 5) / 100)
    valorComDesconto = valorCompra - desconto
    print('Valor da compra: ', valorCompra, '\nValor a Vista: ',valorComDesconto)
else:
    parcelas = input('Informe a quantidade de parcelas!')
    if parcelas == 3:
        acrescimo = ((valorCompra * 8) / 100)
        print('Valor da compra: ', valorCompra, '\nValor a Prazo: ', valorCompra+acrescimo, '\nValor das parcelas: ',
              (valorCompra+acrescimo)/parcelas)

