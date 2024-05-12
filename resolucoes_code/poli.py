# Descrição: Vamos testar se uma palavra é um palíndromo?! 

def verificar_palindromo(palavra):
    # Remover espaços em branco e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Verificar se a palavra é igual à sua reversão
    return palavra == palavra[::-1]

# Solicitar uma palavra como entrada do usuário
entrada_palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Chamar a função verificar_palindromo e exibir o resultado
if verificar_palindromo(entrada_palavra):
    print("Sim, a palavra", entrada_palavra.upper(), "é um palíndromo!")
else:
    print("Não, a palavra", entrada_palavra.upper(), "não é um palíndromo.")

