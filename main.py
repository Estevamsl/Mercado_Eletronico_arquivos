try:

    from meta import Meta
    from time import sleep as sp
    from interface import MetaMain
    from os import(
        
        system as st,
        remove as rm

    )

except (ModuleNotFoundError, ImportError, ImportWarning):
    print('Módulo não encontrado ou importação incorreta')
# st('cls') # Não usar esta função, pois ele corrompe o app

class Mercado(Meta, MetaMain):
    total_compras = 0
    def __init__(self):
        super().__init__()

    def comprar(self, arquivo): # método para comprar coisas no mercado
        # 
        try:
            self.inserir_dinheiro() # Método da classe Meta() para inserir dinheiro para fazer compras no supermercado
        except (

            ModuleNotFoundError,
            ImportError, 
            ImportWarning

        ):
            print('Houve um erro ao importar o método')

        while True:

            # menu1 = Menu() # IntÂncia o Menu()
            self.menu_secundario() # Chama o método menu secundário na classe Menu()
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
                    self.menu_secundario() # Chama o método menu secundário na classe Menu()
            if opcao == 1:
                while True:
                    print(f'''{("PRODUTOS:")}{("VALORES:"):>28}{("QUANTIDADES:"):>25}{("TOTAL:"):>26} {("DATA:"):>20}
\033[35m[1]\033[m \033[36m{(self.Natural)} Unds Natural {("R$3.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.Refri} Unds Refri {("R$5.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.Alcoólica} Unds Alcoólica {("R$50.00"):>30}\033[m
\033[35m[4]\033[m \033[36mVoltar ao menu de compras\033[m
                ''')    

                    while True:
                        try:
                            opcao2 = int(input('Digite sua opcão: '))
                            st('cls') # Não usar esta função, pois ele corrompe o app
                            if opcao2:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)
                            st('cls') # Não usar esta função, pois ele corrompe o app
                            print(f'''{("PRODUTOS:")}{("VALORES:"):>28}{("QUANTIDADES:"):>25}{("TOTAL:"):>26} {("DATA:"):>20}
\033[35m[1]\033[m \033[36m{(self.Natural)} Unds Natural {("R$3.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.Refri} Unds Refri {("R$5.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.Alcoólica} Unds Alcoólica {("R$50.00"):>30}\033[m
\033[35m[4]\033[m \033[36mVoltar ao menu de compras\033[m
                ''') 

                    if opcao2 == 4:
                        break
                    elif opcao2 <= 0 or opcao2 > 4:
                        print('Escolha uma opção de 1 até 4')
                        sp(1)
                        st('cls') # Não usar esta função, pois ele corrompe o app
                
                    
                    if self.dinheiro > 0:
                        if opcao2 == 1 and self.Natural > 0 and self.dinheiro >= 3: # Se o dinheiro for maior que o preço do produto, então pode comprar
                            if self.dinheiro >= 0:
                                print('Você escolheu Natural')
                                self.qtd_Natural += 1
                                self.total += self.qtd_Natural
                                self.Natural -= 1
                                if self.qtd_Natural >= 1:
                                    self.dinheiro -= 3
                                self.tot_compras_em_reais += 3
                                if self.qtd_Natural >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.Natural == 0:
                                    print('O estoque de Natural acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        if self.qtd_Natural > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Natural > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Natural")} {("R$3.00"):>29} {(self.qtd_Natural):>25}')
                                                        a.write('\n')
                                                        # troca = a.replace(('Natural', "")
                                                        # if self.qtd_Natural > 1:
                                                        #     a.write(troca)
                                                        # else:
                                                            
                                                        #     a.write('\n')

                                                    # with open (arquivo, 'r+') as a:
                                                    #     d = a.readlines() 
                                                        
                                                    #     for i in d:
                                                    #         if i != 'Natural':
                                                    #             a.write(f'{("Natural")} {("R$3.00"):>29} {(self.qtd_Natural):>25}')
                                                    #             a.write('\n')
                                                    #             a.truncate()

                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Natural")} {("R$3.00"):>29} {(self.qtd_Natural):>25}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception: # Está dando erro
                                        print('\033[31mHouve um problema no arquivo\033[m')

                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                                
                                
                        elif opcao2 == 2 and self.Refri > 0 and self.dinheiro >= 5: # Se o dinheiro for maior que o preço do produto, então pode comprar:
                            if self.dinheiro >= 0:
                                print('Você escolheu Refri')
                                self.qtd_Refri += 1
                                self.total += self.qtd_Refri
                                self.Refri -= 1
                                if self.qtd_Refri >= 1:
                                    self.dinheiro -= 5
                                self.tot_compras_em_reais += 5
                                if self.qtd_Refri >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.Refri == 0:
                                    print('O estoque de Refri acabou')
                                    self.Refri = 0
                                else:
                                    try:
                                        if self.qtd_Refri > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Refri > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("Refri")} {("R$5.00"):>31} {(self.qtd_Refri):>25}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Refri")} {("R$5.00"):>31} {(self.qtd_Refri):>25}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception: # Está dando erro
                                        print('\033[31mHouve um problema no arquivo\033[m')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.Alcoólica > 0 and self.dinheiro >= 50: # Se o dinheiro for maior que o preço do produto, então pode comprar:
                            if self.dinheiro > 0:
                                print('Você escolheu Alcoólica')
                                self.qtd_Alcoólica += 1
                                self.total += self.qtd_Alcoólica
                                self.Alcoólica -= 1
                                if self.qtd_Alcoólica >= 1:
                                    self.dinheiro -= 50
                                self.tot_compras_em_reais += 50
                                if self.qtd_Alcoólica >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.Alcoólica == 0:
                                    print('O estoque de Alcoólica acabou')
                                    self.Alcoólica = 0
                                else:
                                    try:
                                        if self.qtd_Alcoólica > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Alcoólica > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("Alcoólica")} {("R$50.00"):>28} {(self.qtd_Alcoólica):>24}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Alcoólica")} {("R$50.00"):>28} {(self.qtd_Alcoólica):>24}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception: # Está dando erro
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app

                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                    else:
                        print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                        sp(1)
                        st('cls') # Não usar esta função, pois ele corrompe o app
            
            elif opcao == 2:
                print('Você escolheu Comidas')

            elif opcao == 3:
                print('Você escolheu EletroEletrônico')
                while True: #
                    print(f'''{("PRODUTO")} {("VALOR"):>50}
\033[35m[1]\033[m \033[36m{(self.SamsungJ8)} Unds Samsung Galaxy J8 {("R$1500.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.SamsungJ7} Unds Samsung Galaxy J7 {("R$1300.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.SamsungJ6} Unds Samsung Galaxy J6 {("R$1000.00"):>30}\033[m
\033[35m[4]\033[m \033[36m{self.iphone} Unds Iphone  {("R$3000.00"):>40}\033[m
\033[35m[5]\033[m \033[36m{self.smartTVLG} Unds Smart TV LG {("R$2000.00"):>36}\033[m
\033[35m[6]\033[m \033[36mVoltar ao menu de compras\033[m
                ''')

                    while True:
                        try:
                            opcao2 = int(input('Digite sua opcão: '))
                            st('cls') # Não usar esta função, pois ele corrompe o app
                            if opcao2:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)
                            st('cls') # Não usar esta função, pois ele corrompe o app
                            print(f'''{("PRODUTO")} {("VALOR"):>50}
\033[35m[1]\033[m \033[36m{(self.SamsungJ8)} Unds Samsung Galaxy J8 {("R$1500.00"):>30}\033[m
\033[35m[2]\033[m \033[36m{self.SamsungJ7} Unds Samsung Galaxy J7 {("R$1300.00"):>30}\033[m
\033[35m[3]\033[m \033[36m{self.SamsungJ6} Unds Samsung Galaxy J6 {("R$1000.00"):>30}\033[m
\033[35m[4]\033[m \033[36m{self.iphone} Unds Iphone  {("R$3000.00"):>40}\033[m
\033[35m[5]\033[m \033[36m{self.smartTVLG} Unds Smart TV LG {("R$2000.00"):>36}\033[m
\033[35m[6]\033[m \033[36mVoltar ao menu de compras\033[m
                ''')

                    if opcao2 == 6:
                        print(f'O seu troco é: R${self.dinheiro} reais\n')
                        break
                    elif opcao2 <= 0 or opcao2 > 6:
                        print('Escolha uma opção de 1 até 4')
                    
                    if self.dinheiro > 0:
                        if opcao2 == 1 and self.SamsungJ8 > 0 and self.dinheiro >= 1500: # Se o dinheiro for maior que o preço do produto, então pode comprar::
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J8')
                                self.qtd_SamsungJ8 += 1
                                self.total += self.qtd_SamsungJ8
                                self.SamsungJ8 -= 1
                                if self.qtd_SamsungJ8 >= 1:
                                    self.dinheiro -= 1500
                                self.tot_compras_em_reais += 1500
                                if self.qtd_SamsungJ8 >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.SamsungJ8 == 0:
                                    print('O estoque de Samsung Galaxy J8 acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ8 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ8 > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("Samsung Galaxy J8")} {("R$1500.00"):>22} {(self.qtd_SamsungJ8):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Samsung Galaxy J8")} {("R$1500.00"):>22} {(self.qtd_SamsungJ8):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app
                                
                        elif opcao2 == 2 and self.SamsungJ7 > 0 and self.dinheiro >= 1300: # Se o dinheiro for maior que o preço do produto, então pode comprar::
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J7')
                                self.qtd_SamsungJ7 += 1
                                self.total += self.qtd_SamsungJ7
                                self.SamsungJ7 -= 1
                                if self.qtd_SamsungJ7 >= 1:
                                    self.dinheiro -= 1300
                                self.tot_compras_em_reais += 1300
                                if self.qtd_SamsungJ7 >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.SamsungJ7 == 0:
                                    print('O estoque de Samsung Galaxy J7 acabou')
                                    self.SamsungJ7 = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ7 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ7 > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("Samsung Galaxy J7")} {("R$1300.00"):>22} {(self.qtd_SamsungJ7):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Samsung Galaxy J7")} {("R$1300.00"):>22} {(self.qtd_SamsungJ7):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.SamsungJ6 > 0 and self.dinheiro >= 1000: # Se o dinheiro for maior que o preço do produto, então pode comprar::
                            if self.dinheiro > 0:
                                print('Você escolheu Samsung Galaxy J6')
                                self.qtd_SamsungJ6 += 1
                                self.total += self.qtd_SamsungJ6
                                self.SamsungJ6 -= 1
                                if self.qtd_SamsungJ6 >= 1:
                                    self.dinheiro -= 1000
                                self.tot_compras_em_reais += 1000
                                if self.qtd_SamsungJ6 >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.SamsungJ6 == 0:
                                    print('O estoque de Samsung Galaxy J6 acabou')
                                    self.SamsungJ6 = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ6 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ6 > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("Samsung Galaxy J6")} {("R$1000.00"):>22} {(self.qtd_SamsungJ6):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("Samsung Galaxy J6")} {("R$1000.00"):>22} {(self.qtd_SamsungJ6):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 4 and self.iphone > 0 and self.dinheiro >= 3000: # Se o dinheiro for maior que o preço do produto, então pode comprar::
                            if self.dinheiro >= 0:
                                print('Você escolheu Iphone')
                                self.qtd_iphone += 1
                                self.total += self.qtd_iphone
                                self.iphone -= 1
                                if self.qtd_iphone >= 1:
                                    self.dinheiro -= 3000
                                self.tot_compras_em_reais += 3000
                                if self.qtd_iphone >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.iphone == 0:
                                    print('O estoque de iphone acabou')
                                    self.iphone = 0
                                else:
                                    try:
                                        if self.qtd_iphone > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_iphone > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("iphone")} {("R$3000.00"):>33} {(self.qtd_iphone):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("iphone")} {("R$3000.00"):>33} {(self.qtd_iphone):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 5 and self.smartTVLG > 0 and self.dinheiro >= 2000: # Se o dinheiro for maior que o preço do produto, então pode comprar::
                            if self.dinheiro >= 0:
                                print('Você escolheu Smart TV LG')
                                self.qtd_smartTVLG += 1
                                self.total += self.qtd_smartTVLG
                                self.smartTVLG -= 1
                                if self.qtd_smartTVLG >= 1:
                                    self.dinheiro -= 2000
                                self.tot_compras_em_reais += 2000
                                if self.qtd_smartTVLG >= 1:
                                    print(f'Total de troco: R${self.dinheiro} reais\n')
                                else:
                                    print(f'Você ainda não comprou nada no SuperMercado, seu dinheiro é: R${self.dinheiro} reais\n')
                                if self.smartTVLG == 0:
                                    print('O estoque de smart TV LG acabou')
                                    self.smartTVLG = 0
                                else:
                                    try:
                                        if self.qtd_smartTVLG > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_smartTVLG > 1:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        self.total -= 1 # Pode ser que não de certo
                                                        a.write(f'{("smart TV LG")} {("R$2000.00"):>28} {(self.qtd_smartTVLG):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a+') as a:
                                                        a.write(f'{("smart TV LG")} {("R$2000.00"):>28} {(self.qtd_smartTVLG):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('\033[31mHouve um problema no arquivo\033[m')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                    else:
                        print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                        sp(1)
                        st('cls') # Não usar esta função, pois ele corrompe o app

            elif opcao == 4:
                print('Você escolheu EletroDoméstico')
            elif opcao == 5:
                print('Você escolheu Brinquedos')

            elif opcao == 6:
                # Mercado.total_compras = self.qtd_Natural + self.qtd_Refri + self.qtd_Alcoólica + (self.qtd_SamsungJ8 + self.qtd_SamsungJ7 + self.qtd_SamsungJ6 + self.qtd_iphone + self.qtd_smartTVLG)
                
                
                
                print(f'O seu troco é: R${self.dinheiro} reais')
                
                
                
                
                print(f'Você comprou neste mercado na data: {self.atual}')
                if self.total > 0:
                    if self.total > 1:
                        print(f'QUANTIDADE TOTAL DAS COMPRAS: {(self.total)}\n')
                    else:
                        print(f'QUANTIDADE TOTAL DA COMPRA: {(self.total)}\n')
                sp(2.6)
                try:
                    with open(arquivo, 'a') as a:
                        if self.total == 0:
                            a.write('\n')
                            # a.write(f'TOTAL DE DINHEIRO QUE O USUÁRIO INFORMOU: R${(self.dinheiro)}\n')
                            # a.write(f'TROCO: R${self.tot_compras_em_reais - self.dinheiro}\n')
                            a.write(f'TOTAL GASTO NA COMPRA:{("R$"):>60}{(self.tot_compras_em_reais):>1}.00 Reais\n')
                            a.write(f'DIA DA COMPRA:                                                                                    {(self.atual)}\n')
                            a.write('=-='*36)
                            a.write('\n')
                        if self.total > 0:
                            if self.total > 1:
                                try:
                                    a.write(f'\nQUANTIDADE TOTAL DAS COMPRAS: {(self.total):>22} COMPRAS\n')
                                    a.write(f'TOTAL GASTO NAS COMPRAS:{("R$"):>60}{(self.tot_compras_em_reais):>1}.00 Reais\n')
                                    a.write(f'DIA DAS COMPRAS:                                                                                  {(self.atual)}\n')
                                    a.write('=-='*36)
                                    a.write('\n')
                                except:
                                    print('\033[31mHouve um erro\033[m')
                                    sp(1)
                                    st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                try:
                                    a.write(f'\nQUANTIDADE TOTAL DA COMPRA: {(self.total):>22} COMPRA\n')
                                    a.write(f'TOTAL GASTO NA COMPRA:{("R$"):>60}{(self.tot_compras_em_reais):>1}.00 Reais\n')
                                    a.write(f'DIA DA COMPRA:                                                                                    {(self.atual)}\n')
                                    a.write('=-='*36)
                                    a.write('\n')
                                    a.write('\n')
                                except:
                                    print('\033[31mHouve um erro\033[m')
                                    sp(1)
                                    st('cls') # Não usar esta função, pois ele corrompe o app
                        a.write('\n')
                        a.write('\n')

                except Exception: # ESTÁ DANDO ERRO AQUI

                    print('\033[31mHouve um problema no arquivo\033[m')
                    # sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                self.dinheiro = 0 # depois que eu sair de fazer compras, o dinheiro vai setar em zero
                self.qtd_Natural = self.qtd_Refri = self.qtd_Alcoólica = 0 # depois que eu sair de fazer compras, o dinheiro vai setar em zero
                self.qtd_SamsungJ8 = self.qtd_SamsungJ7 = self.qtd_SamsungJ6 = self.qtd_iphone = self.qtd_smartTVLG = 0 # depois que eu sair de fazer compras, o dinheiro vai setar em zero
                self.total = 0 # depois que fechar de comprar, zera o total das compras

                self.Natural = self.Refri = self.Alcoólica = self.SamsungJ6  = 10
                # ----------ELETRÔNICO----------
                self.SamsungJ8 = self.SamsungJ7 = self.smartTVLG = 20
                self.iphone = 30
        

                
                st('cls') # Não usar esta função, pois ele corrompe o app

                self.total = 0
                break

            else:
                print('Escolha uma opção de 1 até 6')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app