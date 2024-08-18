# Resolvendo Códigos em Python com o Github Copilot

Olá!! Aqui veremos algumas resoluções de códigos em python utilizando o Github Copilot.

### Atenção ⚠️ 

Não tem acesso ao Github Copilot?! Não tem problema!! 
Que tal utilizar o [ChatGPT](https://chat.openai.com/) como seu copiloto de estudos ??

## 1 - Concatenando Dados 🐾

Descrição:
Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?! 
RESULTADO: 
> Solicita o primeiro dado do usuário
<br>
dado1 = input("Por favor, insira o primeiro dado: ")

> Solicita o segundo dado do usuário
<br>
dado2 = input("Por favor, insira o segundo dado: ")

> Concatena os dois dados em uma única string
<br>
resultado = dado1 + dado2

> Exibe o resultado da concatenação
<br>
print("Resultado da concatenação:", resultado)


O que aprenderemos?

* Manipulação de Strings (string)
* Concatenação
* Entrada de dados
* Utilização eficiente do Github Copilot

<br>

## 2 - Repetindo Textos ✏️

Descrição:
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 
RESULTADO:
> Solicita o primeiro número do usuário
<br>
num1 = float(input("Por favor, insira o primeiro número: "))

> Solicita o segundo número do usuário
<br>
num2 = float(input("Por favor, insira o segundo número: "))

> Solicita a operação desejada
<br>
operacao = input("Escolha a operação (+, -, *, /): ")

> Realiza a operação escolhida
<br>
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)
O que aprenderemos?

* Manipulação de Strings (string)
* Números Inteiros (int)
* Múltiplas repetições
* Entrada de dados
* Aproveitar as sugestões do Github Copilot

<br>

## 3 - Operações Matemáticas Simples 📐

Descrição:
Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
RESULTADO:
> Solicita uma string do usuário
<br>
texto = input("Por favor, insira uma string: ")

> Solicita um número inteiro do usuário
<br>
repeticoes = int(input("Por favor, insira um número inteiro: "))

> Repete a string o número de vezes informado
<br>
resultado = texto * repeticoes

> Exibe o resultado
<br>
print("Resultado:", resultado)
O que aprenderemos?

* Operações Matemáticas Básicas
* Entrada de dados
* Utilização eficiente do Github Copilot

<br>

## 4 - Verificando Números Pares e Ímpares 🧮

Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.
RESULTADO:
> Solicita um número inteiro do usuário:
<br>
numero = int(input("Por favor, insira um número inteiro: "))

> Verifica se o número é par ou ímpar usando a operação de módulo
<br>
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

O que aprenderemos?
* Utilização de condicionais em Python (if, else) para realizar verificações.
* Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
* Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código.


<br>

## 5 - Calculando Média de Notas 📚

Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.
RESULTADO:
> Solicita as três notas do usuário
<br>
nota1 = float(input("Por favor, insira a primeira nota: "))
nota2 = float(input("Por favor, insira a segunda nota: "))
nota3 = float(input("Por favor, insira a terceira nota: "))

> Calcula a média das três notas
<br>
media = (nota1 + nota2 + nota3) / 3

> Exibe o resultado da média
<br>
print(f"A média das três notas é: {media:.2f}")

O que aprenderemos?
* Uso de variáveis para armazenar dados fornecidos pelo usuário.
* Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
* Prática na solicitação e manipulação de entrada do usuário.

<br>

## 6 - Verificando Palíndromos 🔄

Descrição: Vamos testar se uma palavra é um palíndromo?! 
Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
RESULTADO:
> Solicita uma palavra do usuário
<br>
palavra = input("Por favor, insira uma palavra: ")

> Converte a palavra para minúsculas para evitar problemas com diferenciação entre maiúsculas e minúsculas
<br>
palavra = palavra.lower()

> Inverte a palavra
<br>
palavra_invertida = palavra[::-1]

> Verifica se a palavra original é igual à palavra invertida
<br>
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")


O que aprenderemos?
* Manipulação de strings em Python, especialmente invertendo uma string.
* Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
* Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.
