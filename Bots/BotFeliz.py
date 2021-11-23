from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            '1': 'Oláa!!',
            '2': 'Como você está? :)',
            '3': 'Pode me ajudar?',
            '4': 'Tchau'}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
        
    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'Meu nome é {self.__nome}! Prazer em conhece-lo!'
    
    def executa_comando(self,cmd):
        print('     --> Eu te respondo: ', end='')
        if cmd == '1':
            print('Oi! Que dia lindo, não é mesmo?!')
        elif cmd == '2':
            print('Estou maravilhosamente feliz!!')
        elif cmd == '3':
            print('Claro que posso! Será um prazer!')
        elif cmd == '4':
            print('Até mais, tenha um bom dia! ')
        else:
            print('Digite um comando válido para eu conseguir te responder!')
            

    def boas_vindas(self):
        return f'--> {self.nome} diz: Que bom que você me escolheu!'

    def despedida(self):
        return f'--> {self.nome} diz: Que pena que você já vai embora, até a próxima!'