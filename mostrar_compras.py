# TRATANDO DE LISTAR COMPRAS
try:

    from os import system as st
    from interface import MetaMenu, Interface
    from time import sleep as sp
    from datetime import date as dt
    from inicio import Inicio
    from menu import Menu

except (ModuleNotFoundError, ImportWarning, ImportError):
    print('Módulo não encontrado ou importação incorreta')

class Compras():
    st('cls')
    def __init__(self):
        super().__init__()

    def __listar_compras__(self): #
        menu1 = Menu()
        while True:
            menu1.menu_secundario()
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
                    menu1.__listar__()
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
                    menu.menu_eletronico()
                    while True:
                        try:
                            opcao = int(input('Digite a sua opção: '))
                            st('cls')
                            if opcao:
                                break
                        except ValueError:
                            print('Digite uma opção válida')
                            sp(1)
                            st('cls')
                    if opcao == 1:
                        pass
            elif opcao == 4:
                print('Você escolheu EletroDoméstico')
            elif opcao == 5:
                print('Você escolheu Brinquedos')
            elif opcao == 6:
                break
            else:
                print('Escolha uma opção de 1 até 6')