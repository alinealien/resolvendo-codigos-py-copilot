# 💻 Algoritmos em Python com GitHub Copilot e Codespaces

## 🎓 Desafio do Curso "Formação GitHub Certification"

**Especialista: Aline Antunes**  
[LinkedIn](https://www.linkedin.com/in/allineantunnes)

## 🔍 Sobre o Desafio
Este repositório faz parte do desafio prático do curso "Formação GitHub Certification", onde exploramos o uso do **GitHub Copilot** e **GitHub Codespaces** para criar e solucionar algoritmos em Python.

A proposta é testar o potencial do Copilot para:
- Auxiliar na escrita de código.
- Corrigir erros durante o desenvolvimento.
- Ajudar na documentação dos projetos.
- Utilizar o Codespaces como ambiente de desenvolvimento na nuvem.

---

## 📚 Estrutura do Projeto
O repositório contém scripts simples que demonstram a criação de algoritmos com o suporte do Copilot:

### 1. [concat_dados.py](concat_dados.py)
Concatena duas entradas do usuário e exibe o resultado.
```python
# Recebendo os dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenando e exibindo o resultado
print("Os dados concatenados são:", dado1 + " " + dado2)
```

### 2. [operacao_mat.py](operacao_mat.py)
Executa operações matemáticas entre dois números inteiros fornecidos pelo usuário.
```python
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operação inválida"

if isinstance(resultado, (int, float)) and resultado < 0:
    resultado = abs(resultado)

print("Resultado:", resultado)
```

### 3. [repetindo_texto.py](repetindo_texto.py)
Repete um texto digitado pelo usuário um número determinado de vezes.
```python
texto = input("Digite um texto: ")
numero = int(input("Digite um número inteiro: "))
print((texto + " ") * numero)
```

---

## 🚀 Como Executar
1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/RP-Lago/algoritmos-python-copilot-codespaces.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd algoritmos-python-copilot-codespaces
   ```
3. Execute os scripts desejados:
   ```bash
   python concat_dados.py
   python operacao_mat.py
   python repetindo_texto.py
   ```

Caso utilize o **GitHub Codespaces**, basta abrir o projeto na nuvem e rodar os scripts diretamente no terminal integrado.

---

## 🧙‍💻 Reflexões sobre o Uso do Copilot
Durante esse desafio, percebi como o **GitHub Copilot** pode facilitar minha produtividade. Ele me ajudou a:
- Gerar código rapidamente a partir de descrições simples.
- Diminuir erros comuns em lógica de programação.
- Melhorar minha compreensão sobre boas práticas.
- Criar uma documentação clara para meus projetos.

O **Codespaces** também se mostrou um ambiente muito útil, permitindo desenvolver diretamente no navegador sem precisar configurar um ambiente local.

Se você também quer melhorar sua eficiência no desenvolvimento, vale a pena explorar essas ferramentas!

🚀 **Bora codar!**

