from Bots.Bot import Bot
from Bots.Comandos import Comandos


class BotTriste(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = [
            Comandos('Oláa!!', 'Oi...'),
            Comandos('Como você está? :)',
                     'Queria sentir algo para te responder...'),
            Comandos('Pode me ajudar?',
                     'Até posso, mas acho que não ajudaria muito de qualquer jeito...'),
            Comandos('Tchau', 'Tchau...')
        ]
        self.__comando_erro = 'Você não digitou um comando válido e estou muito triste :('

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    def apresentacao(self):
        return f'Meu nome, infelizmente, é {self.__nome}...'

    def boas_vindas(self):
        return f'Você tinha que escolher logo o mais inútil?'

    def despedida(self):
        return f'Finalmente você vai se livrar de mim!'
