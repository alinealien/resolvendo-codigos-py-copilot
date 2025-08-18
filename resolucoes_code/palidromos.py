# Solicita a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas para evitar diferenças (ex: 'Ovo' e 'ovo')
palavra_formatada = palavra.lower()

# Inverte a palavra formatada usando slicing [::-1]
palavra_invertida = palavra_formatada[::-1]

# Compara a palavra formatada com a sua versão invertida
if palavra_formatada == palavra_invertida:
  print(f"A palavra '{palavra}' é um palíndromo!")
else:
  print(f"A palavra '{palavra}' não é um palíndromo.")