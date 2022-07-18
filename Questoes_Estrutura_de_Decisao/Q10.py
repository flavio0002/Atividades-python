
"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""
turno = input("M - MATUTINO\nV - VESPERTINO\nN - NOTURNO\n:")

if(turno[0].upper()=='M'):
    print("Bom dia!")
elif(turno[0].upper()=='V'):
    print("Boa tarde!")
elif(turno[0].upper()=='N'):
    print("Boa noite!")
