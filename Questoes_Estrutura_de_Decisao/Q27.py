"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """
quilos_morangos = float(input("Informe a quantidade de quilos de morango: "))
quilos_macas = float(
    input("Informe a quantidade de quilos de morango: "))  # maçãs
preco_macas = 0
preco_morango = 0
if(quilos_morangos > 8):
    if(quilos_morangos <= 5):
        preco_morango = quilos_morangos*2.50
    else:
        preco_morango = quilos_morangos*2.20
    if(preco_morango == 25):
        preco_morango += (preco_morango+(10/100))
if(quilos_macas > 8):
    if(quilos_macas <= 5):
        preco_macas = quilos_macas*1.80
    else:
        preco_macas = quilos_macas*1.50
    if(preco_macas == 25):
        preco_macas += (preco_macas+(10/100))

print("Preço dos morangos é %.2f R$" % (preco_morango))
print("Preço dos maças é %.2f R$" % (preco_macas))
