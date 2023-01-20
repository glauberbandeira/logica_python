indice_poluicao = float(input('Índice de poluição: '))

if (indice_poluicao >= 0.3) and (indice_poluicao < 0.4):
    print(f'Índice de poluição {indice_poluicao}. Grupo 1 suspender atividades.')
elif (indice_poluicao >= 0.4) and (indice_poluicao < 0.5):
    print(f'Índice de poluição {indice_poluicao}. Grupo 2 suspender atividades.')
elif (indice_poluicao >= 0.5):
    print(f'Índice de poluição {indice_poluicao}. Grupo 1 suspender atividades.')
else:
    print('Níveis aceitáveis!')