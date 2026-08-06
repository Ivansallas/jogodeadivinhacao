#Jogo da forca
print("********************************")
print("Bem vindo ao jogo da Foca")
print("********************************")

palavrasecreta = "Abacaxi".upper()
letrasacertadas = ["_"] * len(palavrasecreta)
total_tentativas = len(palavrasecreta)

print(letrasacertadas)

enforcou = False
acertou = False
tentativas = 0

while(not enforcou and not acertou and tentativas < total_tentativas):
    chute = input("Digite uma letra? ")
    chute = chute.strip().upper()

    if(chute in palavrasecreta):
        index = 0
        for letra in palavrasecreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
    else:
        tentativas += 1

    # controle de tentativas
    enforcou = tentativas == total_tentativas
    acertou = "_" not in letrasacertadas
    print("Letras acertadas: {}".format(letrasacertadas))
    print("Tentativas restantes: {}".format(total_tentativas - tentativas))

    if(acertou):
        print("Parabéns, você ganhou!")
    elif(enforcou):
        print("Você perdeu! A palavra era {}".format(palavrasecreta))

print("Fim do jogo")