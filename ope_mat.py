# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Clodoaldo FA
# 10-mar-2025
# Version 00.01.00

def get_user_input_number(prompt):
    """
    Função para obter a entrada numérica do usuário com tratamento de erros.
    :param prompt: Mensagem para o usuário.
    :return: Entrada numérica do usuário.
    """
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def get_user_input_operation(prompt):
    """
    Função para obter a operação matemática do usuário com tratamento de erros.
    :param prompt: Mensagem para o usuário.
    :return: Operação matemática escolhida pelo usuário.
    """
    while True:
        operation = input(prompt).strip()
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Erro: Por favor, insira uma operação válida (+, -, *, /).")

def main():
    """
    Função principal para executar a aplicação.
    """
    try:
        # Obter entradas do usuário
        numero1 = get_user_input_number("Digite o primeiro número: ")
        numero2 = get_user_input_number("Digite o segundo número: ")
        operacao = get_user_input_operation("Escolha a operação matemática (+, -, *, /): ")

        # Executar a operação desejada
        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                alterar_numero = input("Divisão por zero é impossível. Deseja alterar o segundo número? (sim/não): ").strip().lower()
                if alterar_numero == 'sim':
                    numero2 = get_user_input_number("Digite um novo valor para o segundo número: ")
                    resultado = numero1 / numero2
                else:
                    print("Divisão por zero não pode ser realizada. O programa será encerrado. Obrigado!")
                    return
            else:
                resultado = numero1 / numero2

        # Exibir o resultado
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
