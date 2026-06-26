# 🎮 Jogo de Adivinhação

Projeto desenvolvido para a disciplina de **Introdução à Programação**.

O jogador tenta adivinhar um número secreto entre **1 e 50**, escolhendo um nível de dificuldade. A pontuação diminui conforme o chute se distancia do número secreto.

---

## Como jogar

1. Execute o jogo:
   ```bash
   python jogo.py
   ```
2. Escolha o nível de dificuldade:
   | Nível | Tentativas |
   |-------|-----------|
   | Fácil | 20 |
   | Médio | 10 |
   | Difícil | 5 |

3. Digite um número entre **1 e 50** a cada rodada.
4. O jogo indica se o chute foi **maior** ou **menor** que o número secreto.
5. Ao acertar, sua pontuação final é exibida com um feedback de desempenho.

---

## Sistema de pontuação

- Pontuação inicial: **1000 pontos**
- A cada erro, são descontados pontos com base na distância do chute:
  ```
  pontos -= abs(número_secreto - chute)
  ```
- Quanto mais próximo do número secreto, menos pontos você perde.

| Pontuação | Desempenho |
|-----------|------------|
| ≥ 800 | Excelente! |
| ≥ 500 | Bom! |
| < 500 | Pode melhorar... |

---

## Requisitos

- Python 3.x
- Biblioteca `colorama`

```bash
pip install colorama
```

---

## Tecnologias

- Python 3.12
- [colorama](https://pypi.org/project/colorama/) — cores no terminal
