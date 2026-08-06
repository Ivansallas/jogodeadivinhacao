# Jogo da forca
print("********************************")
print("Bem vindo ao jogo da Foca")
print("********************************")

palavrasecreta = "forte"
letrasacertadas = ["_"] * len(palavrasecreta)
total_tentativas = len(palavrasecreta)

enforcou = False
acertou = False
tentativas = 0

while(not enforcou and not acertou and tentativas < total_tentativas):
    chute = input("Digite uma letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavrasecreta:
        if(chute.upper() == letra.upper()):
            letrasacertadas[index] = letra
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    tentativas += 1
    print("Letras acertadas:", letrasacertadas)
    print("Tentativas usadas:", tentativas)

    if "_" not in letrasacertadas:
        acertou = True

print("Fim do jogo")
