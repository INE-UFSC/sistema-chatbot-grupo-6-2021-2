from Bots.Bot import Bot
from Bots.Comandos import Comandos

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [
            Comandos('Oláa!!', 'Oi! Que dia lindo, não é mesmo?!'),
            Comandos('Como você está? :)', 'Estou maravilhosamente feliz!!'),
            Comandos('Pode me ajudar?', 'Claro que posso! Será um prazer!'),
            Comandos('Tchau', 'Até mais, tenha um bom dia! ')
        ]
        self.__comando_erro = 'Digite um comando válido para eu conseguir te responder!'

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
        return f'Meu nome é {self.__nome}! Prazer em conhece-lo!'           

    def boas_vindas(self):
        return f'--> {self.nome} diz: Que bom que você me escolheu!'

    def despedida(self):
        return f'--> {self.nome} diz: Que pena que você já vai embora, até a próxima!'