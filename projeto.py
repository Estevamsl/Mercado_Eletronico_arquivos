# Este é verdadiero projeto
try:

    from menu import Menu
    from App import AppTeste
    from os import(
    
        system as st,
        remove as rm,
        listdir as lt

    )
    from time import sleep as sp
    from interface import MetaProjeto

except (ModuleNotFoundError, ImportError, ImportWarning):
    print('\033[31mNão foi possível importar os módulos\033[m\n')


class Main(AppTeste):
    def __init__(self):
        super().__init__()

    def main(self):
        st('cls')
        arquivo = 'mercado.txt'
        while True:
            self.menu_principal()
            while True:
                try:
                    opcao = int(input('Digite sua opcão: \033[32m'))
                    print('\033[m')
                    sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                    if opcao:
                        break
                except ValueError:
                    print('\033[m\033[31mDigite uma opção inteira\033[m')
                    sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                    self.menu_principal() 

            if opcao == 1:
                self.criar_arquivo(arquivo)

            elif opcao == 2:
                self.__listar_compras__()

            elif opcao == 3:
                self.comprar(arquivo)

            elif opcao == 4:
               self.compras_feitas(arquivo) 

            elif opcao == 5:
                self.deletar_compras(arquivo)

            elif opcao == 6:
                try:
                    rm(arquivo) # remove o arquivo
                except FileNotFoundError:
                    print(f'\033[31mNão foi possível encontrar o arquivo \033[m{arquivo}\033[31m para deletar pois o mesmo não se encontra no repositório ou foi deletado pelo usuário\033[m\n')
                    sp(5.5)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                else:
                    print(f'\033[31mArquivo \033[m{arquivo} \033[31mdeletado com sucesso\033[m\n')
                    sp(1.5)
                    st('cls') # Não usar esta função, pois ele corrompe o app

            elif opcao == 7:
                # st('cls') # Não usar esta função, pois ele corrompe o app
                sp(0.6)
            elif opcao == 8:
                print('\033[32mSaindo...\033[m')
                sp(1)
                break
            else:
                print('\033[31mEscolha uma opção de 1 até 8\033[m\n')


if __name__ == '__main__':
    main1 = Main()
    main1.main()
