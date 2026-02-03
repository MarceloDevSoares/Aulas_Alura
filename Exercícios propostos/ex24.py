peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / altura**2 
print(f'Seu IMC e: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 25:
    print('Você está acima do peso.')
else:
    (print('Seu peso está adequado.'))