
contador_total = 0
contador_sit_1 = 0
contador_sit_2 = 0
contador_sit_3 = 0
contador_sit_4 = 0

id_mouse = int(input('Digite o id do mouse: '))
while id_mouse != 0:
    print('1 - Necessita de esfera.')
    print('2 - Necessita de limpeza.')
    print('3 - Necessita de troca do cabo ou conector.')
    print('5 - Quebrado ou inutilizado.')
    defeito = int(input("Infome o tipo de defeito: "))
    if defeito == 1:
        contador_sit_1 = contador_sit_1 + 1
    elif defeito == 2:
        contador_sit_2 = contador_sit_2 + 1
    elif defeito == 3:
        contador_sit_3 = contador_sit_3 + 1
    elif defeito == 4:
        contador_sit_4 = contador_sit_4 + 1
    contador_total = contador_total + 1
    id_mouse = int(input('Digite o id do mouse: '))

p1 = contador_sit_1 / contador_total * 100
p2 = contador_sit_2 / contador_total * 100
p3 = contador_sit_3 / contador_total * 100
p4 = contador_sit_4 / contador_total * 100
print(f"Quantidade de mouses {contador_total}")
print("Situação                                         Quantidade  Percentual")
print(f"1 - Necessidade de esfera                            {contador_sit_1}        {p1:.2f}%")
print(f"2 - Necessidade de limpeza                           {contador_sit_2}        {p2:.2f}%")
print(f"3 - - Necessita de troca do cabo ou conector.        {contador_sit_3}        {p3:.2f}%")
print(f"4 - Quebrado ou inutilizado.                         {contador_sit_4}        {p4:.2f}%")