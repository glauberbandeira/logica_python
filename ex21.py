# Build an algorithm that reads 10 positive integer values and:
"""
a) find the largest value
b) find the smallest value
c) Calculate the average of the numbers read
"""
maior = -999
menor = 999
soma = 0

for n in range(1, 11):
    valor = int(input('Infome um número: '))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input('Infome um número: '))
media = soma / 10

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'A média dos números é {media}')