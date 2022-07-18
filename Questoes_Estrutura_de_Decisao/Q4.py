"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """
vogal_consoante = input("Digite um letra: ")

if(vogal_consoante[0].upper() == 'A'    or vogal_consoante[0].upper() == 'E' or vogal_consoante[0].upper() == 'I' or
        vogal_consoante[0].upper() == 'O' or vogal_consoante[0].upper() == 'U'):
    print("A letra digitada e uma VOGAL")
else:
    print("A letra digitada e uma CONSOANTE")
