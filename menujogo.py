def escolherjogo():
    print("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌")
    print("───▄▄██▌█░░░░ MENU  ░░░░▌.")
    print("▄▄▄▌▐██▌█░░░░  DE   ░░░░▌.")
    print("███████▌█▄▄▄▄ Jogo  ▄▄▄▄▌")
    print("▀❍▀▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")
    print("Escolha o jogo que deseja jogar:")
    print("[1] - Jogo da Forca")
    print("[2] - jogo de Adivinhação")
    print("[3] - Sair")

    jogo = int(input("Qual jogo você deseja jogar? "))

    match jogo:
        case 1:
            import jogodaforca

            print("Jogando Jogo da Forca")
            jogodaforca.jogar()
        case 2:
            import jogodaadivinhação

            print("Jogando Jogo de Adivinhação")
            jogodaadivinhação.jogar()
        case 3:
            print("sair")
            exit()


if __name__ == "__main__":
    escolherjogo()
