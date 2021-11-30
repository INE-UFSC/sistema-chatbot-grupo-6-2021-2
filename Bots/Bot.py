##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r
from Comandos import Comandos
class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos
        
    def adicionar_comando(self, comando: str, resposta: str):
        self.__comandos.append(Comandos(comando, resposta))

    def remove_comando(self, index):
        self.__comandos.pop(index)
    
    def mostra_comandos(self):
        for index, comando in enumerate(self.__comandos):
            print(f'{index} - {comando.comando}')

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass