"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """
# l = letra
l = input("Digite uma letra: ").upper()

if(l == 'F'):
    print("FEMININO")
elif(l == 'M'):
    print("MASCULINO")
else:
    print("Sexo Invalido")
