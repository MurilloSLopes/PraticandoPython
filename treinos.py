
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
