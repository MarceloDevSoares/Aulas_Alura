hora_atual = int(input('Digite a hora atual (formato 24h): '))

if 8 <= hora_atual < 18:
    print('Acesso permitido')
else:
    print('Acesso negado.')
    