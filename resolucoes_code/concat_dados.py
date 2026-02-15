# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
# Recebendo os dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenando usando f-string (Python 3.6+)
resultado = f"{dado1} {dado2}"

# Exibindo o resultado
print(f"Resultado da concatenação: {resultado}")
