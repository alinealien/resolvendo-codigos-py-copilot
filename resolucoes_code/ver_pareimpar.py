#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outro IA) para melhorar a estrutura do código.

def verifica_par_impar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Exemplo de uso
numero_digitado = int(input("Digite um número inteiro: "))
resultado = verifica_par_impar(numero_digitado)
print(resultado)
