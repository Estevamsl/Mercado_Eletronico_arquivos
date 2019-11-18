# TRATANDO MENUs
try:

    from os import system as st
    # from interface import Interface
    from time import sleep as sp
    from datetime import date as dt

except (ModuleNotFoundError, ImportWarning, ImportError):
    print('Módulo não encontrado ou importação incorreta')

class Menu():
    def __init__(self):
        super().__init__()
        
        self.atual = dt.today()

        self.senha_principal = 2505
        
        self.tot_compras_em_reais = 0
        self.Natural = 10
        self.Refri = 10
        self.Alcoólica = 10
        self.dinheiro = 0

        self.SamsungJ8 = 20
        self.SamsungJ7 = 20
        self.SamsungJ6 = 10
        self.smartTVLG = 20
        self.iphone = 30
        

    def __listar__(self): #
        print(f'''{("PRODUTO")} {("VALOR"):>60}
[1] {(self.Natural)} Unds Natural {("R$3.00"):>30}
[2] {self.Refri} Unds Refri {("R$5.00"):>30}
[3] {self.Alcoólica} Unds Alcoólica {("R$50.00"):>30}
[4] Voltar ao menu pricipal
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
        print('''[1] Bebidas
[2] Comidas
[3] EletroEletrônico
[4] EletroDoméstico
[5] Brinquedos
[6] Sair
                        ''')

    def menu_terciario(self): #
        print(f'''[1] {self.Natural} Unds Natural............................R$3.00
[2] {self.Refri} Unds Refri..................................................R$5.00
[3] {self.Alcoólica} Unds Alcoólica..........................................R$50.00
[4] Voltar ao menu pricipal
                        ''') 


    def menu_eletronico(self): #
        print(f'''{("PRODUTO")} {("VALOR"):>50}
[1] {(self.SamsungJ8)} Unds Samsung Galaxy J8 {("R$1500.00"):>30}
[2] {self.SamsungJ7} Unds Samsung Galaxy J7 {("R$1300.00"):>30}
[3] {self.SamsungJ6} Unds Samsung Galaxy J6 {("R$1000.00"):>30}
[4] {self.iphone} Unds Iphone  {("R$3000.00"):>40}
[5] {self.smartTVLG} Unds Smart TV LG {("R$2000.00"):>36}
[6] Voltar ao menu de compras
                ''')   

    def __listar_compras__(self): # Lista as compras que estão no mercado
        while True:

            self.menu_secundario()

            while True:
                try:
                    opcao = int(input('Digite sua opcão: '))
                    st('cls')
                    if opcao:
                        break
                except ValueError:
                    print('Digite uma opção válida')

            if opcao == 1:
                while True:
                    self.__listar__() # chama o método menu()
                    while True:
                        try:
                            opcao = int(input('Digite sua opcão: '))
                            st('cls')
                            if opcao:
                                break
                        except ValueError:
                            print('Digite uma opção válida')

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
                            st('cls')
                            if opcao:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)

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
