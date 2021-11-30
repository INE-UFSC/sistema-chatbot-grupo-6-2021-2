from Bots.Bot import Bot
from Bots.Comandos import Comandos
class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [
            Comandos('Oláa!!', 'NÃO FALE COMIGO!'),
            Comandos('Como você está? :)', 'COM RAIVA!' ),
            Comandos('Pode me ajudar?', 'NÃO! PEÇA PARA OUTRO! GRRR'),
            Comandos('Tchau', 'SAI LOGO DAQUI!')
        ]

    @property #nao esquecer o decorator
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    @property
    def comandos(self):
        return self.__comandos


    def apresentacao(self):
        return f'Meu nome é {self.__nome}!!! EU TE ODEIO! Não fale comigo.'
    
    def executa_comando(self, cmd: str):
        print('     --> Eu te respondo: ', end='')
        if len(self.__comandos) >= cmd:
            print(self.__comandos[cmd].resposta)
        else:
            print('NÃO EXISTE ESSE COMANDO, IDIOTA!')

    def boas_vindas(self):
        return f'--> {self.nome} diz: Você me escolheu, que ÓDIO!'

    def despedida(self):
        return f'--> {self.nome} diz: Finalmente. NÃO AGUENTAVA MAIS VOCÊ!!!! '