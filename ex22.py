"""
Inform a program that reads a username and password and does not accept the same password as the username,
showing an error message and asking again for the information.
"""
nome = input('Informe o nome: ')
senha = input('Informe sua senha: ')

while senha == nome:
    print('Senha não pode ser igual ao nome')
    nome = input('Informe o nome: ')
    senha = input('Informe sua senha: ')