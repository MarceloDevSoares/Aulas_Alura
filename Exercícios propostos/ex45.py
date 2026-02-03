import datetime

def saudacao(hora):
    if hora < 12:
     return 'Bom dia'
    elif hora < 18:
       return 'Boa tarde'
    else:
       return 'Boa noite'
    
hora_atual = datetime.datetime.now().hour
print(f'Olá, {saudacao(hora_atual)}.')
