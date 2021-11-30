from Bots.Bot import Bot
from Bots.Comandos import Comandos

class BotMarombeiro(Bot):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__comandos = [
            Comandos("Eai frango", "Frango é tu rapaz, tem nem 40 de braço, ta doido!?!"),
            Comandos("Me passa um treino?", "3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)"),
            Comandos("Conselho", "Quer ficar grande? Tem que comer e treinar todo dia!")
        ]
        self.__comando_erro = "Ah isso eu não sei..."

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return "Treino e dieta eu não furo, tá ligado?"

    def boas_vindas(self):
        return "HORA DO SHOW P****!"

    def despedida(self):
        return "Valeu mermão, até a próxima."