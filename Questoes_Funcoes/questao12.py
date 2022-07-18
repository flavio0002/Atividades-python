"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com
os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn
ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres
serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados. """


"""def embaralhar(palavra):
    return palavra[::2] + palavra[::-2]"""


def embaralhar(palavra):
    cont = 0
    contP = len(palavra)-1
    while(cont < len(palavra)):
        print(palavra[contP], end="")
        print(palavra[cont], end="")
        cont += 2
        contP -= 2
    print()


palavra = input("Insira uma palavra: ")
embaralhar(palavra)
