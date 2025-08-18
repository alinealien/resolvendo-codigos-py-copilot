# Solicita o primeiro número e o converte para float
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número e o converte para float
num2 = float(input("Digite o segundo número: "))

# Realiza as operações matemáticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

# Exibe os resultados
print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {subtracao}")
print(f"{num1} * {num2} = {multiplicacao}")
print(f"{num1} / {num2} = {divisao}")