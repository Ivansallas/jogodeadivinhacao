print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numerosecreto = 40

chute = input("Digite o seu número: ")
print("Você digitou: ", chute )

chuteNumerico = int(chute)

#se voce digitar qualquer numero vou verificar se acertou ou errou
if(numerosecreto == chuteNumerico):
    print("Você acertou!")
else:
    print("Você errou!")
    
print("Fim do jogo")