# INTERFACES
from abc import ABCMeta, ABC, abstractmethod
class Interface(ABC):

    # @abc.abstractmethod
    def __listar__(self):
        pass

    # @abc.abstractmethod
    def menu_principal(self):
        pass
    
    # @abc.abstractmethod
    def menu_secundario(self):
        pass

    # @abc.abstractmethod
    def menu_terciario(self):
       pass
    
    # @abc.abstractmethod
    def __listar_compras__(self):
        pass

    # @abc.abstractmethod
    def menu_eletronico(self):
        pass

    # @abc.abstractmethod
    def comprar(self, arquivo):
        pass

    # @abc.abstractmethod
    def __existis__(self, nome): # Ver se o arquivo exista
        pass

    # @abc.abstractmethod
    def criar_arquivo(self, nome): # Cria o arquivo
        pass

    # @abc.abstractmethod
    def deletar_compras(self, nome): # Cria o arquivo
        pass

    # @abc.abstractmethod
    def ler_arquivo(self, nome): # Ler o arquivo criado
        pass

    # @abc.abstractmethod
    def listar_compras(self):
        pass

    # @abc.abstractmethod
    def inserir_dinheiro(self):
        pass

    # @abc.abstractmethod
    def compras_feitas(self, arquivo):
        pass

    # @abc.abstractmethod
    def executavel(self):
        pass


class MetaMenu(Interface, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __listar__(self):
        pass

    @abstractmethod
    def menu_principal(self):
        pass
    
    @abstractmethod
    def menu_secundario(self):
        pass

    @abstractmethod
    def menu_terciario(self):
       pass
    
    @abstractmethod
    def __listar_compras__(self):
        pass

    @abstractmethod
    def menu_eletronico(self):
        pass


class MetaMeta(Interface, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __existis__(self, nome): # Ver se o arquivo exista
        pass

    @abstractmethod
    def criar_arquivo(self, nome): # Cria o arquivo
        pass

    @abstractmethod
    def deletar_compras(self, nome): # Cria o arquivo
        pass

    @abstractmethod
    def ler_arquivo(self, nome): # Ler o arquivo criado
        pass

    # @abstractmethod
    # def listar_compras(self):
    #     pass

    @abstractmethod
    def inserir_dinheiro(self):
        pass

    @abstractmethod
    def compras_feitas(self, arquivo):
        pass


class MetaMain(Interface, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def comprar(self, arquivo):
        pass


class MetaProjeto(Interface, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def main(self):
        pass