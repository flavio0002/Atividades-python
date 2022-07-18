"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos). """

tamanho_MB = float(input("Informe o tamanho do arquivo a ser baixado: "))
velocidade = float(input("Informe a velocidade de download(mbps): "))

mbps = ((tamanho_MB*8)/velocidade)
minutos = (mbps/60)
print("O tempo de download é de: %.2f minutos" % minutos)
