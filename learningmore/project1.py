import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    jogadores = input("Digite o número de jogaderes (2 - 4): ")
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print("Deve estar entre 2 - 4 jogadores.")
    else:
        print("Incorreto, tente de novo.")

pontua_max = 50
jogadores_pontua = [0 for _ in range(jogadores)]

while max(jogadores_pontua) < pontua_max:
    for jogadores_idx in range(jogadores):
        print("\nNumero de Jogadores", jogadores_idx +
              1, "turno acabou de começar!\n")
        print("Sua pontuação total é: ", jogadores_pontua[jogadores_idx], "\n")
        pontuação_atual = 0

        while True:
            deve_roll = input("Você gostaria de rolar (s)? ")
            if deve_roll.lower() != "s":
                break

            value = roll()
            if value == 1:
                print("Você rolou 1! Turno feito!")
                pontuação_atual = 0
                break
            else:
                pontuação_atual += value
                print("Você rolou um: ", value)

            print("Sua pontuação é: ", pontuação_atual)

        jogadores_pontua[jogadores_idx] += pontuação_atual
        print("Sua pontuação total é: ", jogadores_pontua[jogadores_idx])

pontua_max = max(jogadores_pontua)
idx_vitorias = jogadores_pontua.index(pontua_max)
print("Jogador Numero", idx_vitorias + 1, "é o vencedor com uma pontuação de: ", pontua_max)
