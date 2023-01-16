altura = float(input('Qual a sua altura? '))
sexo = input('Qual o seu sexo? (M/F): ')

sexo = sexo.upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (61.1 * altura) - 58
print(f'Seu peso ideal é {round(peso_ideal)}kg')
