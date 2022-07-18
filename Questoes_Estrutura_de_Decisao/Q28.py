"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
     porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
      cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
      e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
       tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. """

tabela = """                      Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg"""
valorTotal = 0
quantQuilos = 0


def fazerPagamento(tpCarne):
    formaPagamento = int(input(
        "Insira a forma de pagamento:\n1 - Dinheiro\n2 - Transferencia\n3 - Cartão Tabajara\n: "))
    pagamento = "Tipo não escolhido"
    valorDesconto = 0
    if(formaPagamento == 3):
        valorDesconto = (5/100)*valorTotal
        pagamento = "Cartão Tabajara"
    elif(formaPagamento == 2):
        pagamento = "Transferencia"
    else:
        pagamento = "Dinheiro"

    print()

    print("Nota Fiscal:\nTipo de carne: %s" % tpCarne, "\nQuantidade (KG): %.2f" % quantQuilos, "\nPreço Total: %.2f" % valorTotal, "R$\nTipo de " +
          "Pagamento: %s" % pagamento, "\nValor Desconto: %.2f" % valorDesconto, "R$\nValor Total a pagar:  %.2f R$" % (valorTotal-valorDesconto))


def carneFileDuplo():
    global quantQuilos
    global valorTotal
    quantQuilos = int(input("Informe a quantidade de Kg de carne: "))
    if(quantQuilos <= 5):
        valorTotal = quantQuilos*4.90
    else:
        valorTotal = quantQuilos*5.80
    fazerPagamento("File Duplo")


def carneAlcatra():
    global quantQuilos
    global valorTotal
    quantQuilos = int(input("Informe a quantidade de Kg de carne: "))
    if(quantQuilos <= 5):
        valorTotal = quantQuilos*5.90
    else:
        valorTotal = quantQuilos*6.80
    fazerPagamento("Alcatra")


def carnePicanha():
    global quantQuilos
    global valorTotal
    quantQuilos = int(input("Informe a quantidade de Kg de carne: "))
    if(quantQuilos <= 5):
        valorTotal = quantQuilos*6.90
    else:
        valorTotal = quantQuilos*7.80
    fazerPagamento("Picanha")


print(tabela)
tipoCarne = input("Escolha o tipo de carne: ")
if(tipoCarne[0].upper() == "F"):
    carneFileDuplo()
elif(tipoCarne[0].upper() == "A"):
    carneAlcatra()
elif(tipoCarne[0].upper() == "P"):
    carnePicanha()
