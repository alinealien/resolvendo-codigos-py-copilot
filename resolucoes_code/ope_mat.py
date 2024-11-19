# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif operacao == '-':
    print (num1, "-", num2, "=", abs(num1 - num2))
elif operacao == '*':
    print(num1, "x", num2, "=", num1 * num2)
elif operacao == '/':
    print (num1, "/", num2, "=", num1 / num2)
else:
    print("Operação Inválida")