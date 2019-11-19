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
                    print(f'''{("PRODUTO")} {("VALOR"):>60}
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
                                self.Natural -= 1
                                self.dinheiro -= 3
                                self.tot_compras_em_reais += 3
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.Natural == 0:
                                    print('O estoque de Bebidas Naturais acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        with open(arquivo, 'a+') as a:
                                            a.write(f'{("Natural")}{("R$3.00"):>30}')
                                            a.write('\n')
                                    except Exception:
                                        print('Houve um problema no arquivo')
                                        sp(1)
                                        st('cls') # Não usar esta função, pois ele corrompe o app

                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                                
                                
                        elif opcao2 == 2 and self.Refri > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Refri')
                                self.Refri -= 1
                                self.dinheiro -= 5
                                self.tot_compras_em_reais += 5
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a+') as a:
                                        a.write(f'{("Refri")} {("R$5.00"):>31}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um problema no arquivo')
                                    sp(1)
                                    st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.Alcoólica > 0:
                            if self.dinheiro > 0:
                                print('Você escolheu Alcoólica')
                                self.Alcoólica -= 1
                                self.dinheiro -= 50
                                self.tot_compras_em_reais += 50
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a+') as a:
                                        a.write(f'{("Alcoólica")}{("R$50.00"):>28}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um problema no arquivo')
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
                                self.SamsungJ8 -= 1
                                self.dinheiro -= 1500
                                self.tot_compras_em_reais += 1500
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                if self.Natural == 0:
                                    print('O estoque de Samsung Galaxy J8 acabou')
                                    self.Natural = 0
                                else:
                                    try:
                                        with open(arquivo, 'a') as a:
                                            a.write(f'{("Samsung Galaxy J8")} {("R$1500.00"):>22}')
                                            a.write('\n')
                                    except Exception:
                                        print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app
                                
                        elif opcao2 == 2 and self.SamsungJ7 > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J7')
                                self.SamsungJ7 -= 1
                                self.dinheiro -= 1300
                                self.tot_compras_em_reais += 1300
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a') as a:
                                        a.write(f'{("Samsung Galaxy J7")} {("R$1300.00"):>22}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um proble no arquivo')
                                    sp(1)
                                    st('cls') # Não usar esta função, pois ele corrompe o app
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 3 and self.SamsungJ6 > 0:
                            if self.dinheiro > 0:
                                print('Você escolheu Samsung Galaxy J6')
                                self.SamsungJ6 -= 1
                                self.dinheiro -= 1000
                                self.tot_compras_em_reais += 1000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a') as a:
                                        a.write(f'{("Samsung Galaxy J6")} {("R$1000.00"):>22}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 4 and self.iphone > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Iphone')
                                self.iphone -= 1
                                self.dinheiro -= 3000
                                self.tot_compras_em_reais += 3000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a') as a:
                                        a.write(f'{("Iphone")} {("R$3000.00"):>33}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um problema no arquivo')
                            else:
                                print(f'Você não pode comprar mais poque o seu dinheiro é: R${self.dinheiro} reais')
                                sp(1)
                                st('cls') # Não usar esta função, pois ele corrompe o app

                        elif opcao2 == 5 and self.smartTVLG > 0:
                            if self.dinheiro >= 0:
                                print('Você escolheu Samsung Galaxy J7')
                                self.smartTVLG -= 1
                                self.dinheiro -= 2000
                                self.tot_compras_em_reais += 2000
                                print(f'Total de troco: R${self.dinheiro} reais\n')
                                try:
                                    with open(arquivo, 'a') as a:
                                        a.write(f'{("Smart TV LG")} {("R$2000.00"):>28}')
                                        a.write('\n')
                                except Exception:
                                    print('Houve um problema no arquivo')
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
                print(f'TOTAL DAS COMPRAS: {("R$")}{(self.tot_compras_em_reais)}.00 Reais')
                print(f'O seu troco é: R${self.dinheiro - self.tot_compras_em_reais} reais')
                print(f'Você comprou neste mercado na data: {self.atual}')
                sp(2.6)
                try:
                    with open(arquivo, 'a') as a:
                        a.write('\n')
                        # a.write(f'TOTAL DE DINHEIRO QUE O USUÁRIO INFORMOU: R${(self.dinheiro)}\n')
                        # a.write(f'TROCO: R${self.tot_compras_em_reais - self.dinheiro}\n')
                        a.write(f'TOTAL DAS COMPRAS:{("R$"):>15}{(self.tot_compras_em_reais):>3}.00 Reais')
                        a.write(f'\nDIA DAS COMPRAS:               {(self.atual)}\n')
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