try:

    from main import Mercado

    from meta import Meta
    from time import sleep as sp

    from abc import (
        ABC,
        abstractmethod
    )
    
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
                    
            