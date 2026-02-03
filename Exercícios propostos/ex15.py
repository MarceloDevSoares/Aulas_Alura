lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)    
    print(f'Médias dos valores: {media}')
except ZeroDivisionError:
    print(f'A Lista está vazia, não é possivel calcular a média.')
except Exeption as e:
    print(f'Ocorreu um erro: {e}')