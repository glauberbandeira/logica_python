# Guessing Game v.1.0 / Jogo da Adivinhação v.1.0

from random import randint
from time import sleep
computador = randint (0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print('Vou penser em um número entrer 0 e 5. Tente Adivinhar')
print('-=-' * 20)
jogador  = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando...')
sleep(3)
print(f'Pense no número {computador}')

if jogador == computador:
    print(f'Parabéns! Você conseguiu me vencer')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')