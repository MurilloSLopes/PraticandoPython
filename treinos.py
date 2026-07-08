
print('Python na Escola de Programação da Alura.\n')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos.\n') 

print('A','L','U','R','A', sep='\n') # Imprime cada letra em uma linha separada 


pi = 3.14159
print(f'O valor arredondade de pi é {pi:.2f}\n')  # Arredonda para 2 casas decimais

def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)

inserir_numero = int(input('digite um numero:'))
if inserir_numero % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')

idade_usuario = int(input('Digite sua idade: '))
if idade_usuario >= 18:
    print('Adulto:acima de 18 anos.')
elif idade_usuario <= 12:
    print('Crianca: 0 a 12 anos;')
else:
    print('Adolescente: 13 a 17 anos;')


usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

#Exercícios
##1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Alice", "Bob", "Charlie", "David"]
anos = [1999, 2026]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in numeros:
    print(numero)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11,2): # O range(1, 11, 2) gera os números ímpares de 1 a 10
    soma_impares += i # Adiciona o número ímpar à soma
    print(soma_impares)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")