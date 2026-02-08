def validar_cpf(cpf):
    #verifica se há caracteres não numéricos primeiro
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    # verifica a quantidade exata de números
    if len(cpf) != 11:
        return "Erro: O CPF veve ter exatamente 11 digitos."
    return "CPF válido."

cpf = input('Digite seu CPF: ')
print(validar_cpf(cpf))