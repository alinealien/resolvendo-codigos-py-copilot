# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = str(input("Digite seu texto aqui: "))
numero = int(input("Agora, digite um número: "))

retorno = (string + " ") * numero

print(retorno)
