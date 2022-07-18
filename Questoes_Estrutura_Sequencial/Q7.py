"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""
base = float(input("Insira a base de um quadrado: "))
altura = float(input("Insira a altura de um quadrado: "))
area = ((base*altura)/2)
print("O dobro da área desse quadrado é %.2f" % (area*2))
