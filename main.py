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
            # st('cls') Não usar esta função, pois ele corrompe o app
            if opcao == 1:
                while True:
                    print(f'''{("PRODUTOS:")}{("VALORES:"):>60}{("QUANTIDADES:"):>30}{("TOTAL:"):>30}
[1] {(self.Natural)} Unds Natural {("R$3.00"):>30}
[2] {self.Refri} Unds Refri {("R$5.00"):>30}
[3] {self.Alcoólica} Unds Alcoólica {("R$50.00"):>30}
[4] Voltar ao menu de compras
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

                    if opcao2 == 4:
                        break
                    elif opcao2 <= 0 or opcao2 > 4:
                        print('Escolha uma opção de 1 até 4')
                        sp(1)
                        st('cls') # Não usar esta função, pois ele corrompe o app
                
                    
                    if self.dinheiro > 0:
                        if opcao2 == 1 and self.Natural > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Natural')
                                self.qtd_Natural += 1
                                self.Natural -= 1
                                self.dinheiro -= 3
                                self.tot_compras_em_reais += 3
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.Natural == 0:
                                    print('O estoque de Natural acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        if self.qtd_Natural > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Natural > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Natural")} {("R$3.00"):>22} {(self.qtd_Natural):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Natural")} {("R$3.00"):>22} {(self.qtd_Natural):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')

                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                                
                                
                        elif opcao2 == 2 and self.Refri > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Refri')
                                self.qtd_Refri += 1
                                self.Refri -= 1
                                self.dinheiro -= 5
                                self.tot_compras_em_reais += 5
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.Refri == 0:
                                    print('O estoque de Refri acabou')
                                    self.Refri = 0
                                else:
                                    try:
                                        if self.qtd_Refri > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Refri > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Refri")} {("R$5.00"):>22} {(self.qtd_Refri):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Refri")} {("R$5.00"):>22} {(self.qtd_Refri):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.Alcoólica > 0:
                            if self.dinheiro > 0:
                                print('Você escolheu Alcoólica')
                                self.qtd_Alcoólica += 1
                                self.Alcoólica -= 1
                                self.dinheiro -= 50
                                self.tot_compras_em_reais += 50
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.Alcoólica == 0:
                                    print('O estoque de Alcoólica acabou')
                                    self.Alcoólica = 0
                                else:
                                    try:
                                        if self.qtd_Alcoólica > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_Alcoólica > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Alcoólica")} {("R$50.00"):>22} {(self.qtd_Alcoólica):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Alcoólica")} {("R$50.00"):>22} {(self.qtd_Alcoólica):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
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
[1] {(self.SamsungJ8)} Unds Samsung Galaxy J8 {("R$1500.00"):>30}
[2] {self.SamsungJ7} Unds Samsung Galaxy J7 {("R$1300.00"):>30}
[3] {self.SamsungJ6} Unds Samsung Galaxy J6 {("R$1000.00"):>30}
[4] {self.iphone} Unds Iphone  {("R$3000.00"):>40}
[5] {self.smartTVLG} Unds Smart TV LG {("R$2000.00"):>36}
[6] Voltar ao menu de compras
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

                    if opcao2 == 6:
                        print(f'O seu troco é: R${self.dinheiro} reais\n')
                        break
                    elif opcao2 <= 0 or opcao2 > 6:
                        print('Escolha uma opção de 1 até 4')
                    
                    if self.dinheiro > 0:
                        if opcao2 == 1 and self.SamsungJ8 > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J8')
                                self.qtd_SamsungJ8 += 1
                                self.SamsungJ8 -= 1
                                self.dinheiro -= 1500
                                self.tot_compras_em_reais += 1500
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.SamsungJ8 == 0:
                                    print('O estoque de Samsung Galaxy J8 acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ8 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ8 > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J8")} {("R$1500.00"):>22} {(self.qtd_SamsungJ8):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J8")} {("R$1500.00"):>22} {(self.qtd_SamsungJ8):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app
                                
                        elif opcao2 == 2 and self.SamsungJ7 > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J7')
                                self.qtd_SamsungJ7 += 1
                                self.SamsungJ7 -= 1
                                self.dinheiro -= 1300
                                self.tot_compras_em_reais += 1300
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.SamsungJ7 == 0:
                                    print('O estoque de Samsung Galaxy J7 acabou')
                                    self.SamsungJ7 = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ7 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ7 > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J7")} {("R$1300.00"):>22} {(self.qtd_SamsungJ7):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J7")} {("R$1300.00"):>22} {(self.qtd_SamsungJ7):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.SamsungJ6 > 0:
                            if self.dinheiro > 0:
                                print('Você escolheu Samsung Galaxy J6')
                                self.qtd_SamsungJ6 += 1
                                self.SamsungJ6 -= 1
                                self.dinheiro -= 1000
                                self.tot_compras_em_reais += 1000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.SamsungJ6 == 0:
                                    print('O estoque de Samsung Galaxy J6 acabou')
                                    self.SamsungJ6 = 0
                                else:
                                    try:
                                        if self.qtd_SamsungJ6 > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_SamsungJ6 > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J6")} {("R$1000.00"):>22} {(self.qtd_SamsungJ6):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("Samsung Galaxy J6")} {("R$1000.00"):>22} {(self.qtd_SamsungJ6):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 4 and self.iphone > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Iphone')
                                self.qtd_iphone += 1
                                self.iphone -= 1
                                self.dinheiro -= 3000
                                self.tot_compras_em_reais += 3000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.iphone == 0:
                                    print('O estoque de iphone acabou')
                                    self.iphone = 0
                                else:
                                    try:
                                        if self.qtd_iphone > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_iphone > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("iphone")} {("R$3000.00"):>22} {(self.qtd_iphone):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("iphone")} {("R$3000.00"):>22} {(self.qtd_iphone):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 5 and self.smartTVLG > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Smart TV LG')
                                self.qtd_smartTVLG += 1
                                self.smartTVLG -= 1
                                self.dinheiro -= 2000
                                self.tot_compras_em_reais += 2000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.smartTVLG == 0:
                                    print('O estoque de smart TV LG acabou')
                                    self.smartTVLG = 0
                                else:
                                    try:
                                        if self.qtd_smartTVLG > 0: # se tiver compras feitas em smasung j8, então...
                                            if self.qtd_smartTVLG > 1:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("smart TV LG")} {("R$2000.00"):>22} {(self.qtd_smartTVLG):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app
                                            else:
                                                try:
                                                    with open(arquivo, 'a') as a:
                                                        a.write(f'{("smart TV LG")} {("R$2000.00"):>22} {(self.qtd_smartTVLG):>22}')
                                                        a.write('\n')
                                                except Exception:
                                                    print('\033[31mHouve um problema\033[m')
                                                    sp(1)
                                                    st('cls') # Não usar esta função, pois ele corrompe o app

                                    except Exception:
                                        print('Houve um problema no arquivo')
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
                print(f'O seu troco é: R${self.dinheiro - self.tot_compras_em_reais} reais')
                print(f'Você comprou neste mercado na data: {self.atual}')
                # print(f'QUANTIDADE TOTAL DAS COMPRAS: {self.Mercado.total_compras}')
                sp(2.6)
                try:
                    with open(arquivo, 'a') as a:
                        # if self.qtd_Natural > 0:
                        #     if self.qtd_Natural > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_Natural} COMPRAS DE BEBIDAS NATURAIS\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_Natural} COMPRA DE BEBIDA NATURAl\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_Refri > 0:
                        #     if self.qtd_Refri > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_Refri} COMPRAS DE BEBIDAS Refri\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_Refri} COMPRA DE BEBIDA Refri\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_Alcoólica > 0:
                        #     if self.qtd_Alcoólica > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_Alcoólica} COMPRAS DE BEBIDAS Alcoólica\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_Alcoólica} COMPRA DE BEBIDA Alcoólica\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app

                        # if self.qtd_SamsungJ8 > 0:
                        #     if self.qtd_SamsungJ8 > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_SamsungJ8} COMPRAS DE SamsungJ8\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_SamsungJ8} COMPRA DE SamsungJ8\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_SamsungJ7 > 0:
                        #     if self.qtd_SamsungJ7 > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_SamsungJ7} COMPRAS DE SamsungJ7\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_SamsungJ7} COMPRA DE SamsungJ7\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_SamsungJ6 > 0:
                        #     if self.qtd_SamsungJ6 > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_SamsungJ6} COMPRAS DE SamsungJ6\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_SamsungJ6} COMPRA DE SamsungJ6\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_iphone > 0:
                        #     if self.qtd_iphone > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_iphone} COMPRAS DE Iphone')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_iphone} COMPRA DE Iphone\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        # if self.qtd_smartTVLG > 0:
                        #     if self.qtd_smartTVLG > 1:
                        #         try:
                        #             a.write(f'\nFORAM {self.qtd_smartTVLG} COMPRAS DE smart TV LG\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app
                        #     else:
                        #         try:
                        #             a.write(f'\nFOi {self.qtd_smartTVLG} COMPRA DE smart TV LG\n')
                        #         except Exception:
                        #             print('\033[31mHouve um problema\033[m')
                        #             sp(1)
                        #             st('cls') # Não usar esta função, pois ele corrompe o app


                        a.write('\n')
                        # a.write(f'TOTAL DE DINHEIRO QUE O USUÁRIO INFORMOU: R${(self.dinheiro)}\n')
                        # a.write(f'TROCO: R${self.tot_compras_em_reais - self.dinheiro}\n')
                        a.write(f'TOTAL DAS COMPRAS:{("R$"):>15}{(self.tot_compras_em_reais):>3}.00 Reais')
                        a.write(f'\nDIA DAS COMPRAS:               {(self.atual)}')
                        a.write(f'\nQUANTIDADE TOTAL DAS COMPRAS: {(self.subtotal):>15}')
                        a.write('\n')
                        a.write('\n')
                except Exception:
                    print('Houve um problema no arquivo')
                    sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                self.dinheiro = 0 # depois que eu sair de fazer compras, o dinheiro vai setar em zero

                
                st('cls') # Não usar esta função, pois ele corrompe o app


                break

            else:
                print('Escolha uma opção de 1 até 6')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app