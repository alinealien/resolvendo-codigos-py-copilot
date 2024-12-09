# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# utilizar o método join para poder separar as strings repetidas
resultado = " ".join([string] * numero)
print(resultado)