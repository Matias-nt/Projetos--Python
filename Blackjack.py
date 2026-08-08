import random


def criar_baralho():
  
    valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    baralho = [] 

    
    for valor in valores:
        for i in range(4):
            baralho.append(valor)

    
    random.shuffle(baralho)

    return baralho 



def valor_carta(carta):
    if carta in ["J", "Q", "K"]:
        return 10          
    elif carta == "A":
        return 11         
    else:
        return int(carta)  


def calcular_pontos(mao):
    total = 0
    for carta in mao:
        total += valor_carta(carta)
    return total



def mostrar_mao(nome, mao):
    total = calcular_pontos(mao)
    print(f"  {nome}: {mao}  →  Total: {total} pontos")


def turno_jogador(nome, mao, baralho):
    print(f"\n--- Vez do {nome} ---")

    while True:
        mostrar_mao(nome, mao)
        total = calcular_pontos(mao)

     
        if total > 21:
            print(f"  ⚠  {nome} ESTOUROU com {total} pontos!")
            break

        
        escolha = input("  Quer mais uma carta? (s/n): ").strip().lower()

        if escolha == "s":
            nova_carta = baralho.pop()  
            mao.append(nova_carta)       
            print(f"  Carta recebida: {nova_carta}")
        elif escolha == "n":
            print(f"  {nome} parou com {total} pontos.")
            break
        else:
            print("  Digite apenas 's' para sim ou 'n' para não.")

    return mao



def determinar_vencedor(pontos1, pontos2):
    print("\n" + "=" * 40)
    print("          RESULTADO FINAL")
    print("=" * 40)
    print(f"  Jogador 1: {pontos1} pontos")
    print(f"  Jogador 2: {pontos2} pontos")
    print("-" * 40)

  
    if pontos1 > 21 and pontos2 > 21:
        print("  Ambos estouraram — EMPATE!")
    elif pontos1 > 21:
        print("  🏆  Jogador 2 venceu! (Jogador 1 estourou)")
    elif pontos2 > 21:
        print("  🏆  Jogador 1 venceu! (Jogador 2 estourou)")
    elif pontos1 > pontos2:
        print("  🏆  Jogador 1 venceu!")
    elif pontos2 > pontos1:
        print("  🏆  Jogador 2 venceu!")
    else:
        print("  🤝  Empate!")

    print("=" * 40)



def jogar():
    print("=" * 40)
    print("       BEM-VINDO AO JOGO 21!")
    print("  Regras: chegue o mais perto de 21")
    print("  sem ultrapassar. J/Q/K=10, A=11.")
    print("=" * 40)


    baralho = criar_baralho()


    mao_jogador1 = [baralho.pop(), baralho.pop()]
    mao_jogador2 = [baralho.pop(), baralho.pop()]


    mao_jogador1 = turno_jogador("Jogador 1", mao_jogador1, baralho)

   
    mao_jogador2 = turno_jogador("Jogador 2", mao_jogador2, baralho)

    
    pontos1 = calcular_pontos(mao_jogador1)
    pontos2 = calcular_pontos(mao_jogador2)

  
    determinar_vencedor(pontos1, pontos2)


    jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()  



if __name__ == "__main__":
    jogar()
