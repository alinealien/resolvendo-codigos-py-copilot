# vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 
def repetir_string(string, vezes):
    return string * vezes

# Solicitar uma string e um número inteiro como entrada do usuário
entrada_string = input("Digite uma string: ")
entrada_numero = int(input("Digite um número inteiro: "))

# Chamar a função repetir_string e exibir o resultado
resultado = repetir_string(entrada_string +" ", entrada_numero)
print("A string repetida ", entrada_numero, "vezes é: ", resultado)