# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

entrada_1 = int(input("Insira um número aqui: "))
entrada_2 = int(input("Insira outro número aqui: "))
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print (entrada_1+entrada_2),

elif operacao == "-":
    print(abs(entrada_1-entrada_2)),

elif operacao == "*":
    print(entrada_1*entrada_2),

elif operacao =="/":
    print(entrada_1/entrada_2)

else: 
    print("operacao_invalida")





    
