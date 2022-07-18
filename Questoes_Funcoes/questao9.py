"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721. """


def reverso(num):
    num = str(num)
    numReverso = ""
    cont = 0
    cont2 = len(num)-1
    while(cont < len(num)):
        numReverso += num[cont2]
        cont += 1
        cont2 -= 1
    return numReverso


"""def reverso(num):
    num = str(num)  # Tranformando variavel numero para String
    # print(type(num))
    return num[::-1]"""


num = int(input("Insira um numero: "))
print(reverso(num))
