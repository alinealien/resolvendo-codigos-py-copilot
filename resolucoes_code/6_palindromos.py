def eh_palindromo(palavra):
    # Remover espaços em branco e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Verificar se a palavra é igual à sua versão invertida
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Exemplo de uso
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")