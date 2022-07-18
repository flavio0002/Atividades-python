"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$"""
valor_hora = float(input("Informe o valor ganho por hora: "))
num_horas = float(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora*num_horas
ir = ((11/100)*salario_bruto)
salario_liquido = (salario_bruto-ir)
inss = ((8/100)*salario_liquido)
salario_liquido -= inss
sindicato = ((5/100)*salario_liquido)
salario_liquido -= sindicato
print("Salário Bruto : %.2f R$" % salario_bruto)
print("IR (11%) : ", ir, " R$")
print("INSS (8%) : ", inss, " R$")
print("Sindicato ( 5%) : ", sindicato, " R$")
print("Sálario Liquido : %.2f R$" % salario_liquido)
