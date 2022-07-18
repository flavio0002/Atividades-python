"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato"""
produto1 = float(input("Informe o preço do primeiro produto: "))
produto2 = float(input("Informe o preço do segundo produto: "))
produto3 = float(input("Informe o preço do terceiro produto: "))

if(produto1<produto2 and produto1< produto3):
    print("COMPRE O PRIMEIRO PRODUTO")
elif(produto2<produto3):
    print("COMPRE O SEGUNDO PRODUTO")
else:
    print("COMPRE O TERCEIRO PRODUTO")
