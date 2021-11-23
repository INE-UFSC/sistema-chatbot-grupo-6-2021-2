from Bots.Bot import Bot

class BotTriste(Bot):
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

    def apresentacao(self):
        return f'Meu nome, infelizmente, é {self.__nome}...'
    
    def executa_comando(self,cmd):
        print('     --> Eu te respondo: ', end='')
        if cmd == '1':
            print('Oi...')
        elif cmd == '2':
            print('Queria sentir algo para te responder...')
        elif cmd == '3':
            print('Até posso, mas acho que não ajudaria muito de qualquer jeito...')
        elif cmd == '4':
            print('Tchau...')
        else:
            print('Você não digitou um comando válido e estou muito triste :(')
            

    def boas_vindas(self):
        return 'Você tinha que escolher logo o mais inútil?'

    def despedida(self):
        return 'Finalmente você vai se livrar de mim!'