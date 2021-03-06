# TRATANDO ARQUIVOS
try:

    from menu import Menu
    from time import sleep as sp
    from os import(
        
        system as st, 
        remove as rm
    
    )
    from interface import MetaMeta

except (ModuleNotFoundError, ImportWarning, ImportError) as e:
    print(f'Módulo {e} não encontrado ou importação incorreta')
    sp(1)
    st('cls') # Não usar esta função, pois ele corrompe o app

class Meta(Menu, MetaMeta):
    def __init__(self):
        super().__init__()
    
    def __existis__(self, nome): # Ver se o arquivo exista 
        try:
            a = open(nome, 'r')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True
    
    def criar_arquivo(self, nome): # Cria o arquivo
        try:
            try:
                with open(nome, 'wt') as a:
                    if self.total > 1:
                        a.write('*-*'*36)
                        a.write(f'\n{("PRODUTOS:"):>1}{("VALORES:"):>28}{("QUANTIDADES:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                        a.write('*-*'*36)
                        a.write('\n\n')
                        a.write('=-='*36)
                        a.write('\n')
                    else:
                        a.write('*-*'*36)
                        a.write(f'\n{("PRODUTO:"):>1}{("VALOR:"):>28}{("QUANTIDADE:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                        a.write('*-*'*36)
                        a.write('\n\n')
                        a.write('=-='*36)
                        a.write('\n')
                    
            except:
                print('\033[31mHouve um problema na criação do arquivo\033[m\n')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app
            else:
                print(f'\033[35mArquivo \033[m{nome} \033[35mcriado com sucesso\033[m\n')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app
        except FileNotFoundError:
            print('Arquivo não existe ou não encontrado')

    def chamar_arquivo(self, nome):
        try:
            try:
                with open(nome, 'a+') as a:
                    if self.total > 1:
                            a.write('*-*'*36)
                            a.write(f'\n{("PRODUTOS:"):>1}{("VALORES:"):>28}{("QUANTIDADES:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                            a.write('*-*'*36)
                            a.write('\n\n')
                            a.write('=-='*36)
                            a.write('\n')
                    else:
                        a.write('*-*'*36)
                        a.write(f'\n{("PRODUTO:"):>1}{("VALOR:"):>28}{("QUANTIDADE:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                        a.write('*-*'*36)
                        a.write('\n\n')
                        a.write('=-='*36)
                        a.write('\n')
            except:
                    print('\033[31mHouve um problema na criação do arquivo\033[m\n')
                    sp(1)
                    st('cls') # Não usar esta função, pois ele corrompe o app
        except FileNotFoundError:
            print('Arquivo Não encontrado ou foi deletado')

    def deletar_compras(self, nome): # deleta compras do carrinho de compras do supermercado
        try:
            try: # tenta deletar as compras se o arquivo existir ou se o arquivo não foi deletado (removido)
                rm(nome)
                try:
                    with open(nome, 'at') as a: # Se o arquivo existir, ele remove as compras do mercado
                        if self.total > 1:
                            a.write('*-*'*36)
                            a.write(f'\n{("PRODUTOS:"):>1}{("VALORES:"):>28}{("QUANTIDADES:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                            a.write('*-*'*36)
                            a.write('\n\n')
                            a.write('=-='*36)
                            a.write('\n')
                        else:
                            a.write('*-*'*36)
                            a.write(f'\n{("PRODUTO:"):>1}{("VALOR:"):>28}{("QUANTIDADE:"):>22}{("TOTAL:"):>26} {("DATA:"):>20}\n')
                            a.write('*-*'*36)
                            a.write('\n\n')
                            a.write('=-='*36)
                            a.write('\n')                    
                except:
                    print(f'\033[31mhouve um problema na remeção das compras no arquivo\033[m {nome}\n')
                    sp(3.5)
                    st('cls') # Não usar esta função, pois ele corrompe o app
                else:
                    print('Não tem compras no seu carrinho')
                    sp(1.5)
                    st('cls') # Não usar esta função, pois ele corrompe o app
            except:
                print(f'\033[31mHouve um problema na remoção das compras do arquivo \033[m{nome} \033[31mpois o mesmo arquivo não existe no repositório ou foi deletado pelo usuário\033[m\n')
                sp(6.5)
                st('cls') # Não usar esta função, pois ele corrompe o app
            else:
                # st('cls')
                print(f'\033[31mCompras no arquivo: \033[m{nome} \033[31mdeletado com sucesso\033[m\n')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app
        except FileNotFoundError:
            print('Arquivo não encontrado ou foi deletado')
        else:
            print(f'Arquivo {nome} ENCONTRADO COM SUCESSO')

    def ler_arquivo(self, nome): # Ler o arquivo criado
        try:
            a = open(nome, 'rt')
        except:
            print('\033[31mErro ao ler o arquivo\033[m\n')
            sp(1)
            st('cls') # Não usar esta função, pois ele corrompe o app
        else:
            print(a.read())

    def compras_feitas(self, arquivo): # Este método mostra o total de compras que foi feito
        try:
            with open(arquivo, 'rt') as a:
                print(a.read())
        except:
            print('\033[31mHouve um problema ao ler o arquivo\033[m\n')
            sp(1)
            st('cls') # Não usar esta função, pois ele corrompe o app

    def inserir_dinheiro(self): # Insere o dinheiro para comprar no supermercado
        while True:
            try:
                dinheiro = float(input('Digite o seu dinheiro: \033[32m'))
                print('\033[m')
                st('cls') # Não usar esta função, pois ele corrompe o app
                if dinheiro:
                    break
            except ValueError:
                print('Digite um dinheiro válido')
                sp(1)
                st('cls') # Não usar esta função, pois ele corrompe o app
        self.dinheiro += dinheiro
