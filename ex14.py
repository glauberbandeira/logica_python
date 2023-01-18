n1 = int(input("Digite primeiro número: "))
n2 = int(input("Digite segundo número: "))
n3 = int(input("Digite terceiro número: "))
n4 = int(input("Digite quarto número: "))

aoquadrado1 = n1 ** 2
aoquadrado2 = n2 ** 2
aoquadrado3 = n3 ** 2
aoquadrado4 = n4 ** 2

if aoquadrado3 >= 100:
    print(f"O número do N3 é maior de 100, então paramos por aqui.")
else:
    print(f"N1:{n1}, N2:{n2}, N3:{n3}, N4:{n4}")