import os

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
    os.system('cls') #os.system cls esta pegando a biblioteca os (importada na primeira linha) e ativando o comando para limpar o terminal
    print('Encerrando app\n')

def escolher_opcao():    
       opcao_escolhida = int(input('Escolha uma opção: ')) #criacao de variavel




       if opcao_escolhida == 1:
           print('Cadastrar restaurantes')
       elif opcao_escolhida == 2:
           print('Listar restaurantes')
       elif opcao_escolhida == 3:     
           print('Ativar restaurantes')
       else:
           finalizar_app()

#bloco para definor o aquivo principal do app
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()