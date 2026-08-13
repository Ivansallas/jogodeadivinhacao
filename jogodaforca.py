import random

# Jogo da forca
print("********************************")
print("Bem vindo ao jogo da Foca")
print("********************************")

#Lendo arquivo de palavras
arquivo = open("palavras.txt", "r")
palavras = []
for linha in arquivo:
    palavras.append(linha.strip().upper())
arquivo.close()

numero = random.randrange(0, len(palavras))
    
palavrasecreta = palavras[numero].upper()
letrasacertadas = ["_"] * len(palavrasecreta)
total_tentativas = len(palavrasecreta)

enforcou = False
acertou = False
tentativas = 0

print("A palavra secreta tem {} letras".format(len(palavrasecreta)))
print(letrasacertadas)

while(not enforcou and not acertou and tentativas < total_tentativas):
    chute = input("Digite uma letra? ")
    chute = chute.strip().upper()
    
    if (chute in palavrasecreta):
        index = 0
        for letra in palavrasecreta:
            if(chute == letra):
                letrasacertadas[index] = letra
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
    else:
        tentativas += 1
        
    enforcou = tentativas == total_tentativas
    acertou = "_" not in letrasacertadas
    print("Letras acertadas:", letrasacertadas)
    print("Tentativas usadas:", tentativas)
    
    # Verifica se o jogador ganhou ou perdeu
    if (acertou):
        print("Parabéns, você ganhou!")
    elif (enforcou):
        print("Você perdeu!")

print("Fim do jogo")
