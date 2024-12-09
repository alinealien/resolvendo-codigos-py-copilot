# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

operacao = input("Escolha uma operação(+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 - numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida!"
else:
    resultado = "Operação inválida!"

print(f"Resultado: {resultado}")

