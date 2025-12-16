# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

somaNotas = nota1 + nota2 + nota3;
mediaNotas = somaNotas / 3;

print("A média do aluno é:", round(mediaNotas, 2))