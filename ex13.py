horas_exedentes = 0
codigo_operario = int(input("Digite seu código: "))
horas_trabalhadas = (float(input("Informe a quantidade de horas trabalhadas: ")))

valor_horas = 10
valor_horas_exedentes = 20

if horas_trabalhadas > 50:
    horas_exedentes = (horas_trabalhadas - 50)
    horas_trabalhadas = (horas_trabalhadas - horas_exedentes)
extra = horas_exedentes * valor_horas_exedentes
salario = horas_trabalhadas * valor_horas
salario_total = salario + extra

print(f'Salário: R${salario}')
print(f'Extra: R${extra}')
print(f'Seu salário total esse mês: R${salario_total}')