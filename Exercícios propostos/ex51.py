valor_produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))
percentual_desconto = (valor_produto * (desconto / 100))
valor_final = (valor_produto - percentual_desconto)

print(f'O valor a pagar é de: {valor_final}')