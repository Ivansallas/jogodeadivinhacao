import jogodaforca
import jogodaadivinhacao

def escolherjogo():
    print("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▌")
    print("───▄▄██▌█░░░░MENU ░░░░▌.")
    print("▄▄▄▌▐██▌█░░░░ DE ░░░░▌.")
    print("███████▌█▄▄▄▄JOGO▄▄▄▄▄▄▌")
    print("▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")
    print("Escolha o jogo que deseja jogar:")
    print("[1] - Jogo da Forca")
    print("[2] - jogo de Adivinhação")

    jogo = int(input("Qual jogo você deseja jogar? "))
    match jogo:
        case 1:
            print("Jogando Jogo da Forca")
            jogodaforca.jogar()
        case 2:
            print("Jogando Jogo de Adivinhação")
            jogodaadivinhacao.jogar()
        case 3:
            print("sair")
            exit()

if __name__ == "__main__":
    escolherjogo()        

