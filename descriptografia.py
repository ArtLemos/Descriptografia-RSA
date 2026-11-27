#Tabela de conversão
dicionario = {
    "A": 11, "B": 12, "C": 13, "D": 14, "E": 15,
    "F": 16, "G": 17, "H": 18, "I": 19, "J": 21,
    "K": 22, "L": 23, "M": 24, "N": 25, "O": 26,
    "P": 27, "Q": 28, "R": 29, "S": 31, "T": 32,
    "U": 33, "V": 34, "W": 35, "X": 36, "Y": 37,
    "Z": 38, " ": 39, ".": 41, ",": 42, "!": 43,
    "?": 44}

#Mensagem para descriptografar
mensagem = [2100,688,1141,409,479,832,380,1895,2319,137,1141,
1570,1715,2189,1064,1514,539,2134,542,452,1202]

#Chaves
d = 13 
n = 2747

#Função que usei para ajudar na descriptografia
def resto(a, n):
    return a - (a // n) * n

#Traduzimos todo o código para uma versão descriptografada (Ainda não é a tradução final)
def descriptografar(mensagem, d, n):
    texto_descriptografado = []

    for i in mensagem:
        expoente = d
        restante = 1
        base = resto(i, n)

        while expoente > 0:
            if expoente - (expoente // 2) * 2 != 0:
                restante = resto(restante * base, n)

            base = resto(base**2, n)
            expoente //= 2

        texto_descriptografado.append(restante)

    return texto_descriptografado

#Concatenamos em um texto só
def concatenar_blocos(texto_descriptografado):
    mensagem_string = list(map(str,texto_descriptografado))
    texto_unido = ""
    for i in mensagem_string:
        texto_unido += i 
    return texto_unido

#Separação 2 em 2
def bloquinhos(texto_unido):
    mensagem_bloquinhos = []
    for i in range(0, len(texto_unido), 2):
        pedaco = texto_unido[i:i+2]
        mensagem_bloquinhos.append(int(pedaco))
    return mensagem_bloquinhos

#Tradução final
def traduzir (mensagem_bloquinhos):
    traducao = []
    mensagem_final = ""

    for i in mensagem_bloquinhos:
        for j in dicionario:
            if int(i) == dicionario[j]:
                traducao.append(j)

    for i in traducao:
        mensagem_final += i

    return mensagem_final

#Corpo do código
texto_descriptografado = descriptografar(mensagem, d, n)

texto_unido = concatenar_blocos(texto_descriptografado)

mensagem_bloquinhos = bloquinhos(texto_unido)

mensagem_final = traduzir(mensagem_bloquinhos)

print(mensagem_final)
