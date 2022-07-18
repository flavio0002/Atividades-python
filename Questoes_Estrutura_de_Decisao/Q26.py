"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. """
litros = float(input("Insira a quantidade de litros: "))
tipo_combustivel = input(
    "ESCOLHA:\nA - álcool\nG - gasolina\nInsira o tipo de combustivel: ")
# gasolina = 2,50
# álcool = 1,90
p = 0  # porcentagem
preco = 0  # preço do tipo de combustivel
if(tipo_combustivel[0].upper() == 'A'):
    preco = litros*1.90
    if(litros <= 20):
        p = 3/100
    else:
        p = 5/100
elif(tipo_combustivel[0].upper() == 'G'):
    preco = litros*2.50
    if(litros <= 20):
        p = 4/100
    else:
        p = 6/100

print("Valor Total -> ", ((preco*p)-preco))
