# Solicita um número inteiro do usuário
numero = int(input("Por favor, insira um número inteiro: "))

# Verifica se o número é par ou ímpar usando a operação de módulo
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
