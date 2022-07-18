"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu 
respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""
lista = []
for y in range(5):
    print("Pessoa %iº" % (y+1))
    for z in range(1):
        idade = int(input("Informe a idade: "))
        altura = float(input("Informe a altura: "))
        lista.append([idade, altura])
lista.reverse()
for idade_altura in lista:
    for i in idade_altura:
        print(i)
