"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. """
dia_semana = ["Domingo", "Segunda", "Terça_Feira", "Quarta-Feira", "Quinta-Feira", "Sexta_Feira", "Sabado"]
num = int(input("Digite um número: "))

print(dia_semana[num-1])
