import time

for tempo in range(10, -1, -1):
    if tempo % 2 == 0:
        print(f'Faltam apenas {tempo} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {tempo} segundos restantes.')
        time.sleep(1)
print('Aproveite a promoção agora!')