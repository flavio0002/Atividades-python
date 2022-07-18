"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso 
contrário, ele será classificado como "Inocente"."""
lista_respostas = []
lista_respostas.append(input("Telefonou para a vítima?: ").lower())
lista_respostas.append(input("Esteve no local do crime?: ").lower())
lista_respostas.append(input("Mora perto da vítima?: ").lower())
lista_respostas.append(input("Devia para a vítima?: ").lower())
lista_respostas.append(input("Já trabalhou com a vítima?: ").lower())
cont = 0
for respostas in lista_respostas:
    if(respostas[0] == 's'):
        cont += 1
if(cont == 2):
    print("Suspeito")
elif(cont == 3 or cont == 4):
    print("Cúmplice")
elif(cont == 5):
    print("Assassino")
else:
    print("Inocente")
