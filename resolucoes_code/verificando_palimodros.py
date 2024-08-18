# Solicita uma palavra do usuário
palavra = input("Por favor, insira uma palavra: ")

# Converte a palavra para minúsculas para evitar problemas com diferenciação entre maiúsculas e minúsculas
palavra = palavra.lower()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
