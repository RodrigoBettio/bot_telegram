import telebot
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env') 

CHAVE_API = os.getenv("CHAVE_API")

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@blábláblá.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! O Rodriguinho te mandou um abraço de volta")

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Certeza de que você é a Lelet? Ela tem ciúmes viu?")
    bot.register_next_step_handler(mensagem, verificar_lelet)

def verificar_lelet(mensagem):
    if mensagem.text.lower() == "sim" and "sou eu":
        bot.send_message(mensagem.chat.id, "Um beijo pra você também bb ❤️")
    else:
        bot.send_message(mensagem.chat.id, "Sabia que você não era ela, sai daqui sua feia! 😡")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço pro Rodriguinho
    /opcao4 Se você for a Lelet, pode me enviar um beijo
    """
    bot.reply_to(mensagem, texto)

bot.polling()