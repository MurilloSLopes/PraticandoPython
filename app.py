import os


print ('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
       ''')

print ('1. Cadastrar restaurantes')
print ('2. Listar restaurantes')
print ('3. Ativar restaurantes')
print ('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: ')) #criacao de variavel

def finalizar_app(): #def usando para definir uma função
    os.system('cls') #os.system cls esta pegando a biblioteca os (importada na primeira linha) e ativando o comando para limpar o terminal
    print('Encerrando app\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurantes')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:     
    print('Ativar restaurantes')
else:
    finalizar_app()