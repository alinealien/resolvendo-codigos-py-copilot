def grade_calculator (firstNota,secondNota, thirdNota):
    return (firstNota + secondNota + thirdNota) / 3

firstNota = float(input("Digite a primeira nota: "))
secondNota = float(input("Digite a segunda nota: "))
thirdNota = float(input("Digite a terceira nota: "))

if(grade_calculator(firstNota, secondNota, thirdNota) > 5): 
    print("Aprovado!!! Parabéns, aluno.")
else:
    print("Reprovado!!! Estude mais.")


