import random

ranking = []

dificuldades = {
    "1": {"nome": "Fácil", "max": 50, "tentativas": 10},
    "2": {"nome": "Médio", "max": 100, "tentativas": 7},
    "3": {"nome": "Difícil", "max": 500, "tentativas": 5}
}

def mostrar_menu():
    print("\n🎮 ===== JOGO DA SORTE =====")
    print("1 - Jogar")
    print("2 - Ver Ranking")
    print("3 - Sair")


def escolher_dificuldade():
    while True:
        print("\nEscolha a dificuldade:")
        print("1 - Fácil (1 a 50 | 10 tentativas)")
        print("2 - Médio (1 a 100 | 7 tentativas)")
        print("3 - Difícil (1 a 500 | 5 tentativas)")

        escolha = input("Opção: ").strip()

        if escolha in dificuldades:
            return dificuldades[escolha]
        else:
            print("⚠️ Opção inválida!")


def calcular_pontos(tentativas_restantes, dificuldade):
    base = {
        "Fácil": 10,
        "Médio": 20,
        "Difícil": 40
    }
    return tentativas_restantes * base[dificuldade]


def mostrar_ranking():
    print("\n🏆 ===== RANKING =====")

    if not ranking:
        print("Nenhum jogador ainda.")
        return

    ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)

    for pos, jogador in enumerate(ranking_ordenado, start=1):
        print(f"{pos}º - {jogador[0]} | {jogador[1]} pontos")


def obter_numero(mensagem):
    while True:
        try:
            valor = input(mensagem).strip()

            if valor == "":
                print("⚠️ Entrada vazia!")
                continue

            return int(valor)

        except ValueError:
            print("❌ Digite apenas números inteiros!")


def jogar():
    nome = input("\nDigite seu nome: ").strip()
    if nome == "":
        nome = "Jogador"

    config = escolher_dificuldade()

    numero_secreto = random.randint(1, config["max"])
    tentativas_restantes = config["tentativas"]

    print(f"\n🔢 Número entre 1 e {config['max']}")
    print("Boa sorte!")

    while tentativas_restantes > 0:

        print(f"\nTentativas restantes: {tentativas_restantes}")
        palpite = obter_numero("Seu palpite: ")

        if palpite < 1 or palpite > config["max"]:
            print(f"⚠️ Digite entre 1 e {config['max']}")
            continue

        diferenca = abs(numero_secreto - palpite)

        if palpite < numero_secreto:
            print("🔼 O número secreto é MAIOR.")
        elif palpite > numero_secreto:
            print("🔽 O número secreto é MENOR.")
        else:
            pontos = calcular_pontos(tentativas_restantes, config["nome"])

            print("\n🎉 PARABÉNS, VOCÊ ACERTOU!")
            print(f"Número secreto: {numero_secreto}")
            print(f"Pontos ganhos: {pontos}")

            ranking.append((nome, pontos))
            return

        if diferenca <= 5:
            print("🔥 Muito quente!")
        elif diferenca <= 15:
            print("🌡️ Quente!")
        else:
            print("❄️ Frio!")

        tentativas_restantes -= 1

    print(f"\n💀 Fim de jogo! O número era {numero_secreto}.")


while True:
    mostrar_menu()
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        jogar()
    elif opcao == "2":
        mostrar_ranking()
    elif opcao == "3":
        print("👋 Até a próxima!")
        break
    else:
        print("⚠️ Opção inválida!")