"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. """
import math

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = float(input("Insiar o terceiro número real: "))

print("a: ", (num1*2)*(num2/2))
print("b: ", (num1*3)+num3)
print("c: ", (math.pow(num3, 3)))
