def converter_telefones(lista):
    return [int(telefone) for telefone in lista]

def verifica_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return'Erro na conversão'
        
    return 'Todos os números foram convertidos corretamente!' 

telefones = ['11967403028', '11967403026', '1191584746', '11998764532']
telefones_convertidos = converter_telefones(telefones)

print(verifica_tipos(telefones_convertidos))