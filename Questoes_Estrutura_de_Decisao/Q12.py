"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00"""
valor_hora = float(input("Informe o valor por hora trabalhada: "))
quant_hora = float(input("Informe a quantidade de hora trabalahada: "))
salario_bruto = (valor_hora*quant_hora)
descontos = 0
if(salario_bruto<=900):
    ir = (salario_bruto*(5/100))
    salario_liquido = (salario_bruto-ir)
    inss = (salario_liquido*(10/100))
    salario_liquido = (salario_liquido - inss)
    fgts = (salario_bruto*(11/100))
    salario_liquido = (salario_liquido + fgts)
elif(salario_bruto>900 and (valor_hora*quant_hora)<=1500):
    ir = (salario_bruto*(5/100))
    salario_liquido = (salario_bruto-ir)
    inss = (salario_liquido*(10/100))
    salario_liquido = (salario_liquido - inss)
    fgts = (salario_bruto*(11/100))
    salario_liquido = (salario_liquido + fgts)
    descontos = (salario_liquido*(5/100))
    salario_liquido = (salario_liquido - descontos)
elif(salario_bruto>900 and (valor_hora*quant_hora)<=2500):
    ir = (salario_bruto * (5 / 100))
    salario_liquido = (salario_bruto - ir)
    inss = (salario_liquido * (10 / 100))
    salario_liquido = (salario_liquido - inss)
    fgts = (salario_bruto * (11 / 100))
    salario_liquido = (salario_liquido + fgts)
    descontos = (salario_liquido * (10 / 100))
    salario_liquido = (salario_liquido - descontos)
else:
    ir = (salario_bruto * (5 / 100))
    salario_liquido = (salario_bruto - ir)
    inss = (salario_liquido * (10 / 100))
    salario_liquido = (salario_liquido - inss)
    fgts = (salario_bruto * (11 / 100))
    salario_liquido = (salario_liquido + fgts)
    descontos = (salario_liquido * (20 / 100))
    salario_liquido = (salario_liquido - descontos)

print("Salário Bruto: (%.0f * %.0f)  :R$%.2f" % (valor_hora, quant_hora, (salario_bruto)))
print("(-) IR (5%s) R$%.2f" % ("%", ir))
print("(-) INSS (5%s) R$%.2f" % ("%", inss))
print("(-) FGTS (5%s) R$%.2f" % ("%", fgts))
print("(-) Total de descontos R$%.2f" % (descontos))
print("(-) Salário Liquido R$%.2f" % (salario_liquido))
