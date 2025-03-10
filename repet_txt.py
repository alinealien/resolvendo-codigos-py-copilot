# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 
# Clodoaldo FA
# 10-mar-2025
# Version 00.01.00

def get_user_input_string(prompt):
    """
    Função para obter a entrada de string do usuário com tratamento de erros.
    :param prompt: Mensagem para o usuário.
    :return: Entrada de string do usuário.
    """
    while True:
        try:
            user_input = input(prompt)
            if not user_input.strip():
                raise ValueError("Entrada não pode ser vazia.")
            return user_input
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente.")
        except Exception as e:
            print(f"Erro inesperado: {e}. Por favor, tente novamente.")

def get_user_input_int(prompt):
    """
    Função para obter a entrada de número inteiro do usuário com tratamento de erros.
    :param prompt: Mensagem para o usuário.
    :return: Entrada de número inteiro do usuário.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                raise ValueError("Número deve ser maior que zero.")
            return user_input
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, insira um número inteiro válido.")
        except Exception as e:
            print(f"Erro inesperado: {e}. Por favor, tente novamente.")

def main():
    """
    Função principal para executar a aplicação.
    """
    try:
        # Obter entradas do usuário
        texto = get_user_input_string("Digite a string: ")
        repeticoes = get_user_input_int("Digite o número de vezes para repetir a string: ")

        # Repetir e exibir a string
        for i in range(repeticoes):
            print(f"{i + 1}: {texto}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
