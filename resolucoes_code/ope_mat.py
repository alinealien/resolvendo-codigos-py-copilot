# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Por favor, insira o primeiro número: "))
num2 = float(input("Por favor, insira o segundo número: "))
operacao = input("Por favor, insira a operação (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-": 
    print(abs(num1 - num2))
elif operacao == "*": 
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Operação inválida")