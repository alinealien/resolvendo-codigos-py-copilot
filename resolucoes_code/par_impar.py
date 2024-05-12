# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicitar um número inteiro como entrada do usuário
entrada_numero = int(input("Digite um número inteiro: "))

# Chamar a função verificar_par_ou_impar e exibir o resultado
resultado = verificar_par_ou_impar(entrada_numero)
print("O número", entrada_numero, "é", resultado)