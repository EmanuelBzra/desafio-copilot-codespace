#Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
# Solicita a string do usuário

string_entrada = input("Digite uma string: ")

# Solicita o número inteiro do usuário
numero_vezes = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = string_entrada * numero_vezes

# Exibe o resultado
print("A string repetida é:", resultado)
