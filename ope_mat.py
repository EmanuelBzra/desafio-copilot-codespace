# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita os dois números inteiros do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Converte os números para seus valores absolutos
numero1 = abs(numero1)
numero2 = abs(numero2)

# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = abs(numero1 - numero2)  # Garantindo que o resultado da subtração seja positivo
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 // numero2  # Usando divisão inteira
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

# Exibe o resultado
print("O resultado é:", resultado)

