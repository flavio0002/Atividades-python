"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação sobre a
     participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
      deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
       "Assassino". Caso contrário, ele será classificado como "Inocente". """


print("Perguntas sobre o crime :")
r1 = input("Telefonou para a vítima? ")
r2 = input("Esteve no local do crime? ")
r3 = input("Mora perto da vítima? ")
r4 = input("Devia para a vítima? ")
r5 = input("Já trabalhou com a vítima?")
print()

cont = 0

if(r1[0].upper() == "S"):
    cont += 1
if(r2[0].upper() == "S"):
    cont += 1
if(r3[0].upper() == "S"):
    cont += 1
if(r4[0].upper() == "S"):
    cont += 1
if(r5[0].upper() == "S"):
    cont += 1

if(cont == 2):
    print("Suspeita")
elif(cont == 3 or cont == 4):
    print("Cúmplice")
elif(cont == 5):
    print("Assassino")
else:
    print("Inocente")
