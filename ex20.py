# Elabore um programa que gera e escreve os númemes ímpares dos números entre 100 e 200.
# Write a program that generates and writes the combined numbers of numbers between 100 and 200.
for n in range(101, 201):
    if n % 2 != 0:
        print(f"Impar: {n}" )