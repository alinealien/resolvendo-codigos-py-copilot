# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 

def calcular_media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

# Solicitar as três notas como entrada do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Chamar a função calcular_media e exibir o resultado
media = calcular_media(nota1, nota2, nota3, nota4)
print("A média das três notas é:", round( media, 2))
