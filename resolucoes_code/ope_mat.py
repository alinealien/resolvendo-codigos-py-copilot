# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def main():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return

    op = input("Escolha a operação (+, -, *, /): ").strip()
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b == 0:
            print("Erro: divisão por zero.")
            return
        resultado = a / b
    else:
        print("Operação não suportada.")
        return

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()