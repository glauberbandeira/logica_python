# A person's first and last name / Primeiro e último nome de uma pessoa

# Digite seu nome completo:
n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print("Muito prazer em te conhecer!")
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu primeiro nome é {nome[len(nome)-1]}')