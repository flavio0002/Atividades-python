"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final
o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada
dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a
cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o
programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato
da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""


menu = """1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
vote:"""

listaVotos = [0, 0, 0, 0, 0, 0]
maior = 0
posicao = 0
cont = 0
while(True):
    voto = int(input(menu))
    print()
    if(voto == 1):
        listaVotos[0] += 1
    elif(voto == 2):
        listaVotos[1] += 1
    elif(voto == 3):
        listaVotos[2] += 1
    elif(voto == 4):
        listaVotos[3] += 1
    elif(voto == 5):
        listaVotos[4] += 1
    elif(voto == 6):
        listaVotos[5] += 1
    elif(voto == 0):
        break

for li in listaVotos:
    if(li > maior):
        maior = li
        posicao = cont
    cont += 1

print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")
print("Windows Server           %i" %
      listaVotos[0], "   %i" % ((listaVotos[0]*100)/sum(listaVotos)), "%")
print("Unix                     %i" %
      listaVotos[1], "   %i" % ((listaVotos[1]*100)/sum(listaVotos)), "%")
print("Linux                    %i" %
      listaVotos[2], "   %i" % ((listaVotos[2]*100)/sum(listaVotos)), "%")
print("Netware                  %i" %
      listaVotos[3], "   %i" % ((listaVotos[3]*100)/sum(listaVotos)), "%")
print("Mac OS                   %i" %
      listaVotos[4], "   %i" % ((listaVotos[4]*100)/sum(listaVotos)), "%")
print("Mac OS                   %i" %
      listaVotos[4], "   %i" % ((listaVotos[4]*100)/sum(listaVotos)), "%")
print("Outro                    %i" %
      listaVotos[5], "   %i" % ((listaVotos[5]*100)/sum(listaVotos)), "%")
print("-------------------     -----")
print("Total                    %i" % sum(listaVotos))
print()


def sistemaOperacipnal(op):
    if(op == 0):
        return "Windows Server"
    elif(op == 1):
        return "Unix"
    elif(op == 2):
        return "Linux"
    elif(op == 3):
        return "NetWare"
    elif(op == 4):
        return "Mac OS"
    elif(op == 5):
        return "Outros"


print("O Sistema Operacional mais votado foi o %s" % sistemaOperacipnal(posicao), "com %i" %
      listaVotos[posicao], "votos, correspondendo a %i" % ((listaVotos[posicao]*100)/sum(listaVotos)), "% dos votos")
