# TRATANDO MENUs
try:

    from os import system as st
    from time import sleep as sp
    from datetime import date as dt
    from inicio import Inicio
    from interface import MetaMenu

except (ModuleNotFoundError, ImportWarning, ImportError):
    print('Módulo não encontrado ou importação incorreta')

class Menu(Inicio, MetaMenu):
    def __init__(self):
        super().__init__()        

    def __listar__(self): #
        print(f'''{("PRODUTO")} {("VALOR"):>60}
\033[35m[1]\033[m \033[36m{(self.Natural)} Unds Natural {("R$3.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.Refri} Unds Refri {("R$5.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.Alcoólica} Unds Alcoólica {("R$50.00"):>30}\033[m
\033[35m[4]\033[m \033[36mVoltar ao menu pricipal\033[m
                ''')

    def menu_principal(self): #
        # self.erro()
        print("""\033[35m[1]\033[m \033[36mCriar arquivo\033[m
\033[35m[2]\033[m \033[36mListar Compras do supermercado\033[m
\033[35m[3]\033[m \033[36mComprar\033[m
\033[35m[4]\033[m \033[36mListar o total das compras\033[m
\033[35m[5]\033[m \033[36mRemover compras do carrinho\033[m 
\033[35m[6]\033[m \033[36mDeletar arquivo\033[m
\033[35m[7]\033[m \033[36mRecuperar arquivo deletado\033[m
\033[35m[8]\033[m \033[36mSair\033[m 
            """)

    def menu_secundario(self): #
        print('''\033[35m[1]\033[m \033[36mBebidas\033[m
\033[35m[2]\033[m \033[36mComidas\033[m
\033[35m[3]\033[m \033[36mEletroEletrônico\033[m
\033[35m[4]\033[m \033[36mEletroDoméstico\033[m
\033[35m[5]\033[m \033[36mBrinquedos\033[m
\033[35m[6]\033[m \033[36mSair\033[m
                        ''')

    def menu_terciario(self): #
        print(f'''[1] {self.Natural} Unds Natural............................R$3.00
[2] {self.Refri} Unds Refri..................................................R$5.00
[3] {self.Alcoólica} Unds Alcoólica..........................................R$50.00
[4] Voltar ao menu pricipal
                        ''') 

    def menu_eletronico(self): #
        print(f'''{("PRODUTO")} {("VALOR"):>50}
\033[35m[1]\033[m \033[36m{(self.SamsungJ8)} Unds Samsung Galaxy J8 {("R$1500.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.SamsungJ7} Unds Samsung Galaxy J7 {("R$1300.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.SamsungJ6} Unds Samsung Galaxy J6 {("R$1000.00"):>30}\033[m
\033[35m[4]\033[m \033[36m{self.iphone} Unds Iphone  {("R$3000.00"):>40}\033[m
\033[35m[5]\033[m \033[36m{self.smartTVLG} Unds Smart TV LG {("R$2000.00"):>36}\033[m
\033[35m[6]\033[m \033[36mVoltar ao menu de compras
                ''')   

    def __listar_compras__(self): # Lista as compras que estão no mercado
        while True:
            self.menu_secundario()
            while True:
                try:
                    opcao = int(input('Digite sua opcão: '))
                    st('cls') # Não usar essa função pois corrompe o programa
                    if opcao:
                        break
                except ValueError:
                    print('Digite uma opção válida')
                    sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app

            if opcao == 1:
                while True:
                    self.__listar__() # chama o método menu()
                    while True:
                        try:
                            opcao = int(input('Digite sua opcão: '))
                            st('cls') # Não usar esta função, pois ele corrompe o app
                            if opcao:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)
                            st('cls') # Não usar esta função, pois ele corrompe o app

                    if opcao == 1:
                        print('Você escolheu Natural')
                    elif opcao == 2:
                        print('Você escolheu Refri')
                    elif opcao == 3:
                        print('Você escolheu Alcoólica')
                    elif opcao == 4:
                        break
                    else:
                        print('Escolha uma opção de 1 até 4')

            elif opcao == 2:
                print('Você escolheu Comidas')
                
            elif opcao == 3:
                print('Você escolheu EletroEletrônico')
                while True:
                    self.menu_eletronico()
                    while True:
                        try:
                            opcao = int(input('Digite a sua opção: '))
                            st('cls') # Não usar essa função pois corrompe o programa
                            if opcao:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)
                            st('cls') # Não usar esta função, pois ele corrompe o app

                    if opcao == 1:
                        print('Você escolheu Samsung Galaxy J8')
                    if opcao == 2:
                        print('Você escolheu Samsung Galaxy J7')
                    if opcao == 3:
                        print('Você escolheu Samsung Galaxy J6')
                    if opcao == 4:
                        print('Você escolheu Iphone')
                    if opcao == 5:
                        print('Você escolheu Smart TV LG')
                    if opcao == 6:
                        break

            elif opcao == 4:
                print('Você escolheu EletroDoméstico')
            elif opcao == 5:
                print('Você escolheu Brinquedos')
            elif opcao == 6:
                break
            else:
                print('Escolha uma opção de 1 até 6')
