macas = int(input('Digite a quantidade de maçãs vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

if bananas > macas:
    print('As bananas tiveram mais vendas.')
elif macas > bananas:
    print('As maçãs tiveram mais vendas.')
else:
    print('As vendas foram iguais.')
