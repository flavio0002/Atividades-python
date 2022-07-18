"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto.
"""

num = int(input("Insira um número: "))

"""cont = 0
while(True):
    if (num == cont):
        print("Ano bissexto")
        break
    cont += 4
    if(cont > num):
        print("Ano não bissexto")
        break"""
if(num % 4 == 0 or num % 4 == 0 or num % 400 == 0):
    print("Ano e bissexto")
else:
    print("Ano não bissexto")
