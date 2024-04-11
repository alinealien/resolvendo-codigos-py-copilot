# Pedir as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Exibir o resultado
if media >= 7:
    print("A média das notas é: ", media, " - Parabéns! Você está aprovado(a)!"),

else:
    print("A média das notas é: ", media, " - Sinto muito. Você precisará se esforçar mais ano que vem.")
      