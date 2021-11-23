from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa, lista_bots):
        self.__empresa=nomeEmpresa
        self.__lista_bots = self.adiciona_bot(lista_bots)
        self.__bot = None
    
    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    @property
    def lista_bots(self):
        return self.__lista_bots

    @lista_bots.setter
    def lista_bots(self, lista):
        self.__lista_bots = lista

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, nome):
        self.__empresa = nome

    
    def adiciona_bot(self, bots):
        for x in bots:
            if isinstance(x, Bot):
                self.__lista_bots.append(x)
            else:
                print(f'{x} não é um bot conhecido')
                
    def boas_vindas(self):
        print(f'Bem-vindo ao sistema da empresa {self.__empresa}')

    def mostra_menu(self):
        print("Os bots disponíveis são: ")
        count = 0
        if len(self.__lista_bots) >= 1:
            for x in self.lista_bots:
                apresentacao = x.apresentacao()
                print(f"{count} - Bot: {x.nome} - Mensagem de apresentação: {apresentacao}")
        else:
            print('Não há nenhum bot disponivel')

    def escolhe_bot(self):
        escolha = int(input('Digite o numero do bot escolhido: '))
        self.__bot = self.__lista_bots[escolha] 

    def mostra_comandos_bot(self):
        bot = self.__bot

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
