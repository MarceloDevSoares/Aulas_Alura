atividade_a = int(input('Informe a quantidade de dias para a atividade A: '))
atividade_b = int(input('informe a qunatidade de dias para a atividade B: '))
atividade_c = int(input('Informe a quantidade de dias para a atividade C: '))

if atividade_a >= 0 and atividade_b >= 0 and atividade_c >= 0:
    total_atividade = atividade_a + atividade_b + atividade_c
    print(f'O tempo total do projeto e de {total_atividade} dias.')

else:
    print('Erro: Os dias não podem ser negativos.')