# Solicita o primeiro número do usuário
num1 = float(input("Por favor, insira o primeiro número: "))

# Solicita o segundo número do usuário
num2 = float(input("Por favor, insira o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)
