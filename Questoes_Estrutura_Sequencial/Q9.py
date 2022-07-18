"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9). """
f = float(input("Informe a temperatura em graus Fahrenheit: "))
print("A temperatura de graus(Celsius) é de %.1f" % (5*((f-32)/9)))
