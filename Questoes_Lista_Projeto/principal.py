"""1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, 
está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este 
problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos 
usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo 
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

    Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco 
    ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere 
    um relatório, chamado relatório.txt, no seguinte formato: 

ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB            16,85%
2    anderson       1187,99 MB            46,02%
3    antonio         117,73 MB             4,56%
4    carlos           87,03 MB             3,37%
5    cesar             0,94 MB             0,04%
6    rosemary        752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

    O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
    caso sejam necessários, de forma a agilizar a execução do programa. A conversão da 
    espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma 
    função separada, que será chamada pelo programa principal. O cálculo do percentual de 
    uso também deverá ser feito através de uma função, que será chamada pelo programa principal. """

# método que abre um arquivo do sistema e pega o seu conteudo


def pega_texto_arq():
    listaNomes = []
    for linha in arq.readlines():
        listaNomes.append(linha)
    arq.close()
    return listaNomes


# método para retirar nome e tamanho em uma lista
def retira_nome_tamanho():
    i = 1
    novo_usu = []
    global tamanho_total
    global media
    # poderia ter usado o metodo split() mais como ja fiz a implementação, deixarei-o
    for nome in lista_nomes_tamanho_arq:
        linha_nome = ""
        linha_tamanho = ""
        cont = 0

        for l in nome:
            if(l != " "):
                if(cont == 0):
                    linha_nome += l
                else:
                    linha_tamanho += l
            else:
                cont = 1
        # soma de total de espaço ultilizado
        tamanho_total += espaco_ultilizado(float(linha_tamanho))
        tamanho = float(linha_tamanho)
        novo_usu.append([i, linha_nome, espaco_ultilizado(tamanho)])
        i += 1
    return novo_usu


def espaco_ultilizado(tamanho):
    return float(tamanho/(1024*1024))


# Função que retorna a media de espaço ocupado
def media_tamanho_total():
    return tamanho_total/quant


# função que retorna a porcentagem de cada usúario
def porcentagem_usuario(MB):
    return ((MB*100)/tamanho_total)


# retorna os dados dos usuarios, insere no relatório e faz o calculo de porcentagem
def dados_usuarios():
    dados = ""
    for usu in usuarios:
        dados += "%i    %s       %.2f MB            %.2f \n" % (
            usu[0], usu[1], usu[2], porcentagem_usuario(usu[2]))
    return dados


# Cria o relatorio em memória
def criar_relatorio():
    relatorio = open("relatorio.txt", "w")
    relatorio.write(
        "ACME Inc.           Uso do espaço em disco pelos usuários\n" +
        "------------------------------------------------------------------------\n" +
        "Nr.  Usuário        Espaço utilizado     % do uso\n" +
        "%sEspaço total ocupado: %.2f MB\nEspaço médio ocupado: %.2f MB" % (dados_usuarios(), tamanho_total, media))
    relatorio.close()

    # Iniciando
arq = open('usuarios.txt', 'r')
tamanho_total = 0
media = 0
# Pegando dados do arquivo.txt e inserindo em uma lista
lista_nomes_tamanho_arq = pega_texto_arq()
# inserir cada usuario com atributos em uma lista de usúarios
usuarios = retira_nome_tamanho()
quant = len(usuarios)
media = media_tamanho_total()
# Chamando a função criar relatorio
criar_relatorio()
# mostrando relatorio
relatorio = open("relatorio.txt")
for linha in relatorio.readlines():
    print(linha, end="")
print()
