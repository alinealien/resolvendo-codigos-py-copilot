palavra = input("Digite a palavra a ser verificada: ")

pInvertida = palavra[::-1]

if palavra == pInvertida:
    print(f"A palavra {palavra} é um palíndromo, pois permanece a mesma quando invertida: {pInvertida}.")
else:
    print(f"A palavra {palavra} não é um palíndromo, pois a mesma se altera quando invertida: {pInvertida}.")