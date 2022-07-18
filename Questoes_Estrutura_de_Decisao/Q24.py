"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. """
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

operacao = int(input((
    "Qual operação deseja realizar:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n:")))
if(operacao == 1):
    print("Soma - >", (num1+num2))
elif(operacao == 2):
    print("Subtração - >", (num1-num2))
elif(operacao == 3):
    print("Multiplicação - >", (num1*num2))
elif(operacao == 4):
    print("Divisão - >", (num1/num2))
else:
    print("Opção invalida...")
