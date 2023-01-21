maior = 0

valor = int(input('Receber número: '))

while valor != 0:
    if valor > maior:
        maior = valor
    valor = int(input('Receber número: '))
print(f'Maior valor {maior}')