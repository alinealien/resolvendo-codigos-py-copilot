def verificar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    
    if palavra == palavra_invertida:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")