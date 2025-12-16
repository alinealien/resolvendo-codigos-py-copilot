# Vamos testar se uma palavra ou frase é um palíndromo.
import re
import unicodedata

def normalizar_texto(texto: str) -> str:
    texto = texto.strip().lower()
    # remover acentuação (ex: 'ã' -> 'a')
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(ch for ch in texto if not unicodedata.combining(ch))
    # remover caracteres especiais (pontuação, espaços, etc.) usando re.sub
    texto = re.sub(r'[^a-z0-9]', '', texto)
    return texto

entrada = input("Por favor, insira uma palavra ou frase: ")
texto_limpo = normalizar_texto(entrada)
texto_invertido = texto_limpo[::-1]

if texto_limpo and texto_limpo == texto_invertido:
    print("A entrada é um palíndromo.")
else:
    print("A entrada não é um palíndromo.")