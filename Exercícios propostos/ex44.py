def contador_palavras(palavra):
    return len(palavra)

texto = input('Digite uma palavra: ')
print(f'Essa palavra tem {contador_palavras(texto)} letras.')