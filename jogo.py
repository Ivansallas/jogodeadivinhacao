# Trabalho de introdução a programação
# Parte3

import random
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.CYAN + "********************************")
print(Fore.CYAN + "********************************")
print(Fore.CYAN + "Bem vindo ao jogo de Adivinhação")
print(Fore.CYAN + "********************************\n")
print(Fore.CYAN + "********************************\n")

numerosecreto = random.randrange(1, 51)
totaldetentativas = 0
pontos = 1000

print(Fore.YELLOW + "Escolha o nível de dificuldade:")
print("(1) Fácil   - 20 tentativas")
print("(2) Médio   - 10 tentativas")
print("(3) Difícil -  5 tentativas")

try:
    nivel = int(input(Fore.YELLOW + "Defina o nível: "))
except ValueError:
    print(Fore.RED + "Entrada inválida! Encerrando o jogo.")
    exit()

if nivel == 1:
    totaldetentativas = 20
elif nivel == 2:
    totaldetentativas = 10
elif nivel == 3:
    totaldetentativas = 5
else:
    print(Fore.RED + "Nível inválido! Escolha 1, 2 ou 3. Encerrando o jogo.")
    exit()

acertou = False

while totaldetentativas > 0:
    print(Fore.CYAN + f"\nVocê tem {totaldetentativas} tentativa(s) | Pontos: {pontos}")

    try:
        chuteNumerico = int(input(Fore.WHITE + "Digite um número entre 1 e 50: "))
    except ValueError:
        print(Fore.RED + "Entrada inválida! Digite apenas números inteiros.")
        continue

    if chuteNumerico < 1 or chuteNumerico > 50:
        print(Fore.RED + "Número fora do intervalo! Digite um valor entre 1 e 50.")
        continue

    print(f"Você digitou: {chuteNumerico}")

    if chuteNumerico == numerosecreto:
        acertou = True
        print(
            Fore.GREEN + f"\nParabéns! Você acertou! Pontuação final: {pontos} pontos."
        )
        break
    elif chuteNumerico > numerosecreto:
        print(Fore.RED + "Você errou! O seu chute foi maior que o número secreto.")
    else:
        print(Fore.RED + "Você errou! O seu chute foi menor que o número secreto.")

    pontos -= abs(numerosecreto - chuteNumerico)
    totaldetentativas -= 1

if not acertou:
    print(
        Fore.RED + f"\nSuas tentativas acabaram! O número secreto era {numerosecreto}."
    )

if acertou:
    if pontos >= 800:
        print(Fore.GREEN + "Desempenho: Excelente!")
    elif pontos >= 500:
        print(Fore.YELLOW + "Desempenho: Bom!")
    else:
        print(Fore.YELLOW + "Desempenho: Pode melhorar...")

print(Fore.CYAN + "\nFim do jogo.")
