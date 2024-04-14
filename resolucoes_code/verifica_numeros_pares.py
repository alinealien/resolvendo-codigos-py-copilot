
# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

# Solicitando um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")