"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. """
salario = float(input("Digite o seu salário: "))

if(salario<=280):
    valor_reajuste = (salario+((20/100)*salario))
    reajuste = 20
elif(salario>280 and salario<=700):
    valor_reajuste = (salario + ((15/100) * salario))
    reajuste = 15
elif(salario>700 and salario<=1500):
    valor_reajuste = (salario + ((10/100) * salario))
    reajuste = 10
else:
    valor_reajuste = (salario + ((5/100) * salario))
    reajuste = 5

print("Salario ante do reajuste -> %.2f R$" % (salario))
print("percentual -> %.2f" % reajuste)
print("Valor aumentado -> %.2f R$" % (salario*(reajuste/100)))
print("Valor Total -> %.2f R$" % (valor_reajuste))
