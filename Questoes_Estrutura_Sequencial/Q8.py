"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. """
ganho_hora = float(input("Informe o valor ganho por hora: "))
total_horas = float(input("Informe a quanridade de horas trabalhadas: "))

print("O valor do salário mensal é de %.2f R$" % (total_horas*ganho_hora))
