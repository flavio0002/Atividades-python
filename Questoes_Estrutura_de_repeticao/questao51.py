"""Faça um programa que mostre os n termos da Série a seguir:

      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

    Imprima no final a soma da série. """

"""n1 = 1
n2 = 1
n1_lista = []
n2_lista = []
print("S = ", end="")
while n1 <= 10 - 1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))"""


from operator import concat
listaN1 = []
listaN2 = []

n1 = 1
n2 = 1
txt = "S = "

while (n1 < 10):
    listaN1.append(n1)
    listaN2.append(n2)
    txt += str(n1) + "/" + str(n2) + " + "
    n1 += 1
    n2 += 2
print(txt,  n1, "/", n2, " = ", sum(listaN1), "/", sum(listaN2))
