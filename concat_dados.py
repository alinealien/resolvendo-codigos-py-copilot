# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?! 
# Clodoaldo FA
# 10-mar-2025
# Version 00.01.00

def get_user_input(prompt):
    """
    Função para obter a entrada do usuário com tratamento de erros.
    :param prompt: Mensagem para o usuário.
    :return: Entrada do usuário.
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

def main():
    """
    Função principal para executar a aplicação.
    """
    try:
        # Obter entradas do usuário
        primeiro_dado = get_user_input("Digite o primeiro dado: ")
        segundo_dado = get_user_input("Digite o segundo dado: ")

        # Concatenar os dados
        resultado = primeiro_dado + " " + segundo_dado

        # Exibir o resultado
        print(f"Resultado da concatenação: {resultado}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
