firstInputNumber = int(input('Digite a primeira entrada: '))
secondInputNumber = int(input('Digite a segunda entrada: '))
ariathmetic = input('Digite a operação: ex: +, -, *, / ')
def operation(dia:str):
    match dia:
        case '+':
            return firstInputNumber + secondInputNumber
        case '-':
            return abs(firstInputNumber - secondInputNumber)
        case '*':
            return firstInputNumber * secondInputNumber
        case '/':
            return firstInputNumber / secondInputNumber
        case _:
            return "Valor inválido"
        
result = operation(ariathmetic)
print(result)