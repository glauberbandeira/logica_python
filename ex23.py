"""
Develop a table generator, capable of generating the table of any integer between 1 and 10. The user must inform which
number he wants to var the table. the output should be as in the example below:
"""

numero = int(input('Informe um número entre 1 e 10: '))

while numero < 1 or numero > 10:
    print('Número deve ser menor do que 10')
    numero = int(input('Informe um número: '))
print(f"Tabuada de {numero}")
for n in range(1, 11):
    valor = numero * n
    print(f"{numero} x {n} = {valor}")
