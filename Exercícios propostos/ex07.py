# Solicite um nome de usuário e uma senha e use uma estrutura [if else] para verificar se o nome de usuário e senha fornecidos correspondem aos valores esperados determinados por você.

usuario_correto = 'mdsoares'
senha_correta = '&123321&'

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login bem sucedido!')
else:
    print('Credenciais invalidas. Tente novamente.')