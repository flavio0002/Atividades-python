"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O
usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""


class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def aumentar_canal(self, numero):
        if(numero >= 0 and numero <= 200):
            self.numero_canal = numero
            print("Canal alterado")
        else:
            print(
                "Falha ao alterar o canal...verifique o número digitado deve ser de 0 a 200")

    def aumentar_volume(self, volume):
        if(volume <= 100 and volume > self.volume):
            self.volume = volume
            print("Volume alterado")
        else:
            print("Impossivel aumentar o volume")

    def diminuir_volume(self, volume):
        if(volume >= 0 and volume < self.volume):
            self.volume = volume
            print("Volume alterado")
        else:
            print("Impossivel diminuir o volume")


tv01 = TV(10, 51)
while(True):
    print("opções ---------")
    print("1 - mudar canal")
    print("2 - aumentar volume")
    print("3 - diminuir volume")
    print("4 - desligar\n ---------------")
    op = int(input("Selecionar:"))

    if (op == 1):
        tv01.aumentar_canal(int(input("Insira o canal desejado: ")))

    elif (op == 2):
        tv01.aumentar_volume(int(input("Insira o volume desejado: ")))

    elif(op == 3):
        tv01.diminuir_volume(int(input("Insira o canal desejado: ")))

    elif (op == 4):
        print("Desligando ...")
        break

    else:
        print("Selecione uma opção válida!")
