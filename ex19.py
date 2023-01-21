# Faça um algoritimo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: Múltiplo de 10
# Make an algorithm that counts from 1 to 100 and every multiple of 10 sends a message: Multiple of 10.
for n in range(1, 101):
    print(n)
    if n % 10 == 0:
        print("Multiplo de 10")
