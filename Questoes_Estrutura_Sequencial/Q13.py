"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que 
calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 """
h = float(input("informe a altura:"))

print("Altura ideal:")
print("Homem - %.2f" % ((72.7*h)-58))
print("Mulher - %.2f" % ((62.1*h)-44.7))
