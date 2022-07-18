"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser 
armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""
lista_numeros = []
inverso = []
soma = 0
acima_media = 0
abaixo_sete = 0
while(True):
    numero = int(input("Insira um número: "))
    if(numero == -1):
        break
    lista_numeros.append(numero)
print("A quantidade de nýmeros lidos foi", len(lista_numeros)+1)
print()
print("números em ordem informados:")
for numeros in lista_numeros:
    print(numeros, end=" ")
print()
inverso = lista_numeros
inverso.reverse()
soma = sum(lista_numeros)
media = (sum(lista_numeros)/(len(lista_numeros)+1))
print("números em ordem inversa:")
for numeros in inverso:
    print(numeros, end=" ")
print()
print("A soma dos valores é ", soma)
print("A média dos valores dos números inseridos é %.2f" % (media))
for numeros in lista_numeros:
    if(numeros > media):
        acima_media += 1
    if(numeros < 7):
        abaixo_sete += 1
print("Acima da média -> ", acima_media)
print("Abaixo da sete -> ", abaixo_sete)
print("Programa encerrado..............")
