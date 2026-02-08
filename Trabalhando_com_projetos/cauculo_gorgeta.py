valor_conta = float(input('Digite o valor da conta: '))
percentual_gorgeta = float(input('Digite a porcentagem da gorgeta: '))

valor_gorgeta = valor_conta * percentual_gorgeta/100
total = valor_gorgeta + valor_conta
print(f'Valor da gorgeta: R$ {valor_gorgeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
