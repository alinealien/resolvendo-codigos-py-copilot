# Solicita um número e o converte para inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o resto da divisão por 2 é igual a 0
if numero % 2 == 0:
  # Se for, o número é par
  print(f"O número {numero} é PAR.")
else:
  # Se não for, o número é ímpar
  print(f"O número {numero} é ÍMPAR.")