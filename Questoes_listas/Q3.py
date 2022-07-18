"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""
v = []
for x in range(4):
    v.append(float(input("Digite uma nota: ")))

media = ((sum(v)/4))
print("A média é -> ", media)
