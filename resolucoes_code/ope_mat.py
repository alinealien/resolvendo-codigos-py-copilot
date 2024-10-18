# Vamos solicitar como entrada dois números e depois realizar uma operação simples entre eles.
num = []
soma = 0

# Solicitar dois números do usuário
for i in range(2):
    numero = int(input("Digite um número: "))
    print("\n")
    num.append(numero)
    soma += numero

print("\n")
print("O resultado da soma entre esses números é: " + str(soma))
