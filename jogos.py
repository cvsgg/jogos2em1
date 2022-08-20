import forca
import adivinhacao

def jogar():
    print("Bem vindo! Esolha seu jogo")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))
    if  (jogo == 1):
        print("Inicializando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Inicializando Adivinhação")
        adivinhacao.jogar()
if (__name__ == "__main__"):
    jogar()