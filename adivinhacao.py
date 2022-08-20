def jogar():
    import random

    print ("Bem vindo ao jogo")
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade:")
    print("(1)Fácil, (2)Intermediário (3)Difícil")
    nivel = int(input("Defina o nível:"))
    if (nivel ==1):
        total_de_tentativas = 20
        print ("Fácil")
    elif (nivel==2):
        total_de_tentativas = 10
        print("intermediário")
    else:
        total_de_tentativas = 5
        print("difícil")

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str= input("Digite um numero:")
        print("Você Digitou" , chute_str)
        chute = int(chute_str)
        if(chute > 100 or chute < 1):
            print("Dígite um número entre 1 e 100")
            continue

        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)
        acertou = (chute == numero_secreto)
        if (acertou):
            print("Você acertou! Sua pontuação foi de {}".format(pontos))
            break
        else:
            if (maior):
                print("você errou, seu numero foi maior")
            elif (menor):
                print("você errou, seu numero foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")

if (__name__ == "__main__"):
    jogar()


