# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com o original.

def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Verifica se é um palíndromo
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Exemplo de uso
entrada = input("Digite uma palavra: ")
if eh_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
