# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.


# Solicita o primeiro número do usuário
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número do usuário
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação selecionada pelo usuário
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    # Verifica se o divisor não é zero para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

# Exibe o resultado da operação
print("O resultado é:", resultado)
