from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            '1': 'Oláa!!',
            '2': 'Como você está? :)',
            '3': 'Pode me ajudar?',
            '4': 'Tchau'}

    @property #nao esquecer o decorator
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def apresentacao(self):
        return f'Meu nome é {self.__nome}!!! EU TE ODEIO! Não fale comigo.'
    
    def executa_comando(self, cmd: str):
        print('     --> Eu te respondo: ', end='')
        if cmd == '1':
            print('NÃO FALE COMIGO!')
        elif cmd == '2':
            print('COM RAIVA!')
        elif cmd == '3':
            print('NÃO! PEÇA PARA OUTRO! GRRR')
        elif cmd == '4':
            print('SAI LOGO DAQUI!')
        else:
            print('ESSE COMANDO NÃO EXISTE, IDIOTA!')

    def boas_vindas(self):
        return 'Você me escolheu, que ÓDIO!'

    def despedida(self):
        return 'Finalmente. NÃO AGUENTAVA MAIS VOCÊ!!!! '