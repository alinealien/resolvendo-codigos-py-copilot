# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = input("Digite uma string: ")
inteiro = int(input("Digite um número inteiro: "))

for x in range(inteiro):
    print(string)

print((string + " ") * inteiro)