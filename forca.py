import random
def jogar():
    imprime_abertura()
    palavra_secreta = imprime_palavras_aleatorias()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = inputa_chutes()
        if (chute) in palavra_secreta:
            marca_acerto(chute, letras_acertadas,palavra_secreta)
        else:
            erros = erros + 1

        enforcou = erros ==6
        acertou = ("_") not in letras_acertadas
        print(letras_acertadas)
        if (acertou):
            imprime_acertou()
        if (enforcou):
            imprime_errou()


def imprime_errou():
        print("Você perdeu")

def imprime_acertou():
        print("Você Venceu!")

def marca_acerto(chute, letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

def inputa_chutes():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def imprime_abertura():
    print("Bem vindo ao jogo da forca!! o<-<")

def imprime_palavras_aleatorias():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if (__name__ == "__main__"):
    jogar()