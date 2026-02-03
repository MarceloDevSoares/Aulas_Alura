idade = int(input('Digite a sua idade: '))

if idade >= 10: 
    altura = int(input('Informe a sua altura: '))
    
    if idade >= 10 and altura > 1.50:
        print('Pemitido o acesso da criança no briquedo.')
    elif idade >= 10 and altura < 1.50:
        print('Proíbido acesso da criança no brinquedo.')
else: 
    print('Você não deveria estar aqui.')
        
