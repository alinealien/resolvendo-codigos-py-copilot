# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que repetir a string o número de vezes indicado pelo número inteiro.

texto = input("Por favor, insira uma string: ")
numero = int(input("Por favor, insira um número inteiro: "))

resultado = (texto + " ") * numero

print("O resultado da repetição é: ", resultado) 