numeros = input('Digite os números separados por espaço: ').split()

numeros_pares = filter(lambda x: int(x) % 2 == 0, numeros)

print('Números pares:',' '.join(numeros_pares))

