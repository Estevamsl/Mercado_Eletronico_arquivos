# Este é verdadiero projeto
try:

    from menu import Menu
    from main import Mercado
    from os import(
    
        system as st,
        remove as rm,
        listdir as lt

    )
    from meta import Meta
    from time import sleep as sp
    # from interface import MetaProjeto

except (ModuleNotFoundError, ImportError, ImportWarning):
    print('\033[31mNão foi possível importar os módulos\033[m\n')

class Main(Mercado):
    def __init__(self):
        super().__init__()

    def executavel(self):
        while True:
            try:
                senha = int(input('Digite a sua senha: \033[32m'))
                print('\033[m')
                st('cls')
                if senha:
                    break
            except ValueError:
                print('\033[31mDigite uma senha válida\033[m')
                sp(1)
                st('cls')


        if self.senha_principal == senha:
            # st('cls')
            # sp(0.7)
            print('\033[32mEntrada com sucesso\033[m')
            sp(1.1)
            st('cls')
            def main():
                arquivo = 'mercado.txt'
                compras = Mercado()
                meta1 = Meta()
                menu2 = Menu()
                while True:
                    menu2.menu_principal()
                    while True:
                        try:
                            opcao = int(input('Digite sua opcão: \033[32m'))
                            print('\033[m')
                            sp(1)
                            st("cls")
                            if opcao:
                                break
                        except ValueError:
                            print('\033[m\033[31mDigite uma opção inteira\033[m')
                            sp(1)
                            st('cls')
                            menu2.menu_principal()
                    if opcao == 1:
                        meta1.criar_arquivo(arquivo)

                    elif opcao == 2:
                        menu2.__listar_compras__()

                    elif opcao == 3:
                        compras.comprar(arquivo)

                    elif opcao == 4:
                        meta1.compras_feitas(arquivo) 

                    elif opcao == 5:
                        meta1.deletar_compras(arquivo)

                    elif opcao == 6:
                        try:
                            rm(arquivo) # remove o arquivo
                        except FileNotFoundError:
                            print('\033[31mNão foi possível encontrar o arquivo pois o mesmo não se encontra no repositório ou foi deletado\033[m\n')
                            sp(2.5)
                            st('cls')

                    elif opcao == 7:
                        st('cls')
                        sp(0.6)
                    elif opcao == 8:
                        st('cls')
                        sp(1)
                        print('\033[32mSaindo...\033[m')
                        sp(1)
                        st('cls')
                        break
                    else:
                        print('\033[31mEscolha uma opção de 1 até 8\033[m\n')
            main()
        else:
            print('Não pode executar este arquivo por causa da senha inválida')

    
        

if __name__ == '__main__':
    main1 = Main()
    main1.executavel()