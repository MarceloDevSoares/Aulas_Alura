# Solicite ao usuário que insira um número e, em seguida, use uma estrutura [if else] para determinar se o número é par ou impar.

numero = int(input('Digite o número: '))
if numero % 2 == 0:
    print('o número é par.')
else:
    print('O número é ímpar.')