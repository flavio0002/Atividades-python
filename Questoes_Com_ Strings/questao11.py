"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!
"""
import random
arquivo = open("arq.txt", "r")


# Função para pegar uma palavra aleatória dentro do arquivo
def palavraSecreta():
    palavra = []
    for x in random.choice(arquivo.readlines()):
        if x != '\n':
            palavra.append(x)
    return palavra


# chamando a funcção com a palavra secreta
pScret = palavraSecreta()
# adicionando '_' onde for letra na palavra secreta para mostra para o usuário
letraAcertada = ['_' for x in pScret]
# transformando lista em string
respota = "".join(pScret)
# contador
cont = 0

# Mostrando na tela que é o jogo da forca
print("===  jogo da forca === \nPalavra:", end=' ')
print(letraAcertada)
while True:

    p = input("\nDigite uma letra: ")
    # verificando se tem uma letra igual a que o cara digitou na palavra secreta
    for i in pScret:
        if i == p:
            a = pScret.index(p)
            letraAcertada[a] = p
            pScret[a] = 0

    # verificando se a letra que o cara digitou tem na palavra secreta
    if p not in respota:
        cont += 1
        print("-> Você errou pela ", cont, "° vez. Tente de novo!")

    # mostrando as letras acertadas
    print(letraAcertada)

    # Adivionado em palavalida as letras que foi acertada para forma a palavra certa
    palavalida = ""
    for i in letraAcertada:
        palavalida += i

    # Para o loop
    if respota == palavalida:
        print("\nParabéns você acertou a palavra")
        break
    if cont == 6:
        print("\nVocê foi enforcado ^_^")
        break


arquivo.close()
