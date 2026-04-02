import random

# Criar baralho completo
naipes = ["♠", "♥", "♦", "♣"]
valores = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

def criar_baralho():
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    random.shuffle(baralho)
    return baralho

def calcular_total(mao):
    total = sum(valores[carta[0]] for carta in mao)
    ases = sum(1 for carta in mao if carta[0] == "A")
    
    while total > 21 and ases:
        total -= 10
        ases -= 1
        
    return total

def mostrar_mao(nome, mao, esconder=False):
    if esconder:
        print(f"{nome}: [??] {mao[1][0]}{mao[1][1]}")
    else:
        cartas = " ".join([f"{c[0]}{c[1]}" for c in mao])
        print(f"{nome}: {cartas} (Total: {calcular_total(mao)})")

def blackjack():
    saldo = 100
    
    print("🎰 Bem-vindo ao Blackjack PRO!\n")
    
    while saldo > 0:
        print(f"\n💰 Seu saldo: R${saldo}")
        
        try:
            aposta = int(input("Quanto deseja apostar? "))
        except:
            print("Valor inválido!")
            continue
        
        if aposta > saldo or aposta <= 0:
            print("Aposta inválida!")
            continue
        
        baralho = criar_baralho()
        
        jogador = [baralho.pop(), baralho.pop()]
        dealer = [baralho.pop(), baralho.pop()]
        
        print("\n🃏 Distribuindo cartas...\n")
        
        # Mostrar mãos iniciais
        mostrar_mao("Você", jogador)
        mostrar_mao("Dealer", dealer, esconder=True)
        
        # Verificar blackjack natural
        if calcular_total(jogador) == 21:
            print("🔥 BLACKJACK! Você ganhou 1.5x a aposta!")
            saldo += int(aposta * 1.5)
            continue
        
        # Turno do jogador
        while True:
            if calcular_total(jogador) > 21:
                print("💥 Você estourou!")
                saldo -= aposta
                break
            
            escolha = input("Digite (c) comprar | (p) parar: ").lower()
            
            if escolha == "c":
                carta = baralho.pop()
                jogador.append(carta)
                print(f"Você comprou: {carta[0]}{carta[1]}")
                mostrar_mao("Você", jogador)
            elif escolha == "p":
                break
            else:
                print("Opção inválida!")
        
        # Turno do dealer
        if calcular_total(jogador) <= 21:
            print("\n🤖 Turno do dealer...\n")
            mostrar_mao("Dealer", dealer)
            
            while calcular_total(dealer) < 17:
                carta = baralho.pop()
                dealer.append(carta)
                print(f"Dealer comprou: {carta[0]}{carta[1]}")
        
            total_jogador = calcular_total(jogador)
            total_dealer = calcular_total(dealer)
            
            print("\n📊 Resultado:")
            mostrar_mao("Você", jogador)
            mostrar_mao("Dealer", dealer)
            
            if total_dealer > 21 or total_jogador > total_dealer:
                print("🎉 Você ganhou!")
                saldo += aposta
            elif total_jogador < total_dealer:
                print("😢 Você perdeu!")
                saldo -= aposta
            else:
                print("🤝 Empate!")
        
        # Continuar?
        continuar = input("\nQuer jogar novamente? (s/n): ").lower()
        if continuar != "s":
            break
    
    print("\n🏁 Fim de jogo!")
    print(f"💰 Saldo final: R${saldo}")

# Rodar jogo
blackjack()