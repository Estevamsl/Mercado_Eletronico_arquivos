# POR DENTRO DOS PANOS
try:

    from datetime import date as dt

except (ModuleNotFoundError, ImportWarning, ImportError):
    print('Módulo não encontrado ou importação incorreta')

class Inicio():
    def __init__(self):
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