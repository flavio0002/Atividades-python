"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. """
import sys


print("CAIXA ELETRONICO:")
valor_saque = float(input("Insira o valor a ser retirado: "))
valor_incluido_notas = 1
cont_notas100 = 0
cont_notas50 = 0
cont_notas10 = 0
cont_notas5 = 0
cont_notas1 = 0
if(valor_saque <= 0 or valor_saque >= 600):
    print("Valor de saque fora dos padrões, insira novamente...")
    sys.exit()
else:
    while(valor_incluido_notas <= valor_saque):
        if(valor_incluido_notas+100 <= valor_saque):
            cont_notas100 += 1
            valor_incluido_notas = valor_incluido_notas + 100
        elif((valor_incluido_notas+50) <= valor_saque):
            cont_notas50 += 1
            valor_incluido_notas = valor_incluido_notas + 50
        elif((valor_incluido_notas+10) <= valor_saque):
            cont_notas10 += 1
            valor_incluido_notas = valor_incluido_notas + 10
        elif((valor_incluido_notas+5) <= valor_saque):
            cont_notas5 += 1
            valor_incluido_notas = valor_incluido_notas + 5
        else:
            cont_notas1 += 1
            valor_incluido_notas = valor_incluido_notas + 1

print("Notas de 100 -> ", cont_notas100)
print("Notas de 50 -> ", cont_notas50)
print("Notas de 10 -> ", cont_notas10)
print("Notas de 5 -> ", cont_notas5)
print("Notas de 1 -> ", cont_notas1)
