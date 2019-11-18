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

st('cls')
class Main(Mercado):
    def __init__(self):
        super().__init__()

    def main(self):
        
        arquivo = 'mercado.txt'
        meta1 = Meta()
        while True:
            self.menu_principal()
            while True:
                try:
                    opcao = int(input('Digite sua opcão: \033[32m'))
                    print('\033[m')
                    sp(1)
                    # st("cls")
                    if opcao:
                        break
                except ValueError:
                    print('\033[m\033[31mDigite uma opção inteira\033[m')
                    sp(1)
                    st('cls')
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
                    print('\033[31mNão foi possível encontrar o arquivo pois o mesmo não se encontra no repositório ou foi deletado\033[m\n')
                    sp(2.5)
                    # st('cls')

            elif opcao == 7:
                # st('cls')
                sp(0.6)
            elif opcao == 8:
                st('cls')
                sp(1)
                print('\033[32mSaindo...\033[m')
                sp(1)
                # st('cls')
                break
            else:
                print('\033[31mEscolha uma opção de 1 até 8\033[m\n')


if __name__ == '__main__':
    main1 = Main()
    main1.main()
