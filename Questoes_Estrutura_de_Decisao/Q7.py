"""Faça um Programa que leia três números e mostre o maior e o menor deles."""
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if(num1>num2 and num1 >num3):
    maior = num1
elif(num2>num3):
    maior = num2
else: maior = num3
if(num1<num2 and num1<num3):
    menor = num1
elif(num2<num3):
    menor = num2
else: maior = num3
print("Maior: ", maior)
print("Menor: ", menor)
