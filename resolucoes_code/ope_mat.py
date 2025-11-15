# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# A operação a ser realizada será escolhida pelo usuário.
# As operações disponíveis serão: soma, subtração, multiplicação e divisão.
def calcular(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."