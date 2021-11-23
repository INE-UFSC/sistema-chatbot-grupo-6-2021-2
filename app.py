#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Onion"), BotFeliz("Sunflower")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
