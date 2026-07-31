#Jogo da forca
print("********************************")
print("Bem vindo ao jogo da Foca")
print("********************************")

palavrasecreta = "forte"
letrasacertadas = ["_", "_", "_", "_", "_", "_"]

enforcou = False
acertou = true

while(not enforcou and not acertou):
    chute = input("Digite uma letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavrasecreta:
        if(chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    print("jogando")    

print("Fim do jogo")