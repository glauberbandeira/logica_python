peso_peixe = float(input("Peso do peixe em kg: "))

exesso = 0
multa = 0

if peso_peixe > 50:
    exesso = peso_peixe - 50
    multa = exesso * 4
    print(f"Peso do peixe: {peso_peixe}kg, Exesso: {exesso}kg, Valor da Multa R${multa}")
else :
    print(f"Peso do peixe: {peso_peixe}kg, Não haverá multa.")