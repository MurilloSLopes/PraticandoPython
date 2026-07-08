import os

restaurantes = [{'nome':'Praca', 'categoria': 'Japonesa', 'ativo': False},
                 {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                 {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}] 

#def usando para definir uma função
def exibir_nome_do_programa():
    print ('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
       ''')

def exibir_opcoes():
    print ('1. Cadastrar restaurantes')
    print ('2. Listar restaurantes')
    print ('3. Ativar restaurantes')
    print ('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\ndigite uma tecla para voltar ao menu principal ')
    main() #chamando a funcao main para voltar ao menu principal

def opcao_invalida():
    print('opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante) #adicionando o nome do restaurante na lista de restaurantes
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal() #chamando a funcao voltar_ao_menu_principal para voltar ao menu principal

def lista_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes: #for usando para percorrer a lista de restaurantes
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal() #chamando a funcao voltar_ao_menu_principal para voltar ao menu principal



def alterar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restauranre')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes: #for usando para percorrer a lista de restaurantes
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #alterando o estado do restaurante usando o operador not
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante nao foi encontrado')
        



    voltar_ao_menu_principal

def escolher_opcao():   
    try: #try usando para "tentar" executar o bloco que esta abaixo.
        opcao_escolhida = int(input('Escolha uma opção: ')) #criacao de variavel




        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:     
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:     
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida() #except usando para caso o try nao funcione ele vai executar tal funcao

#bloco para definir o aquivo principal do app
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()