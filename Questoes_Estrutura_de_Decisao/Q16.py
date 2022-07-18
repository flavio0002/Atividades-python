"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O 
programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """
import sys


a = int(input("Insira o valor de A: "))
if(a == 0):
    print("Não e equação do segundo grau...")
    sys.exit()
else:
    b = int(input("Insira o valor de B: "))
    c = int(input("Insira o valor de C: "))
    d = (b**2 - 4*a*c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)

    print('O valor de x1 é {}'.format(x1))
    print('O valor de x2 é {}'.format(x2))
