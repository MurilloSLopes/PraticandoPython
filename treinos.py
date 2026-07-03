
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
