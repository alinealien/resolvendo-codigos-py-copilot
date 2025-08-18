# Solicita as três notas e as converte para float
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Soma as notas
soma_das_notas = nota1 + nota2 + nota3

# Calcula a média dividindo a soma por 3
media = soma_das_notas / 3

# Exibe a média, formatando para duas casas decimais
print(f"A média das notas é: {media:.2f}")