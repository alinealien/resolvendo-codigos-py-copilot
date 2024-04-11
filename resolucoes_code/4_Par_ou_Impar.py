import random


def jogo_par_ou_impar():
    print("Vamos jogar Par ou Ímpar!")
    jogador = input("Escolha Par (P) ou Ímpar (I): ").upper()
    while jogador not in ['P', 'I']:
        jogador = input("Escolha inválida. Escolha Par (P) ou Ímpar (I): ").upper()

    numero_jogador = int(input("Escolha um número entre 0 e 10: "))
    while numero_jogador < 0 or numero_jogador > 10:
        numero_jogador = int(input("Número inválido. Escolha um número entre 0 e 10: "))

    numero_computador = random.randint(0, 10)
    print("O computador escolheu o número:", numero_computador)

    soma = numero_jogador + numero_computador
    resultado = soma % 2

    if resultado == 0:
        print("A soma é", soma, "que é par.")
        if jogador == 'P':
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    else:
        print("A soma é", soma, "que é ímpar.")
        if jogador == 'I':
            print("Você ganhou!")
        else:
            print("Você perdeu!")

jogo_par_ou_impar()