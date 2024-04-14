# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitando a string do usuário
texto = input("Por favor, insira uma string: ")

# Solicitando o número de vezes que a string será repetida
# Convertendo a entrada para um número inteiro
numero_repeticoes = int(input("Por favor, insira o número de vezes para repetir a string: "))

# Repetindo a string o número de vezes informado
texto_repetido = texto * numero_repeticoes

# Exibindo o resultado
print("Resultado:", texto_repetido)