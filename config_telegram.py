import telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("ITOKEN")
chat_id = os.getenv("CHAT_ID")

class TelegramSend:

    def __init__(self, name):
        self.name = name

    def telegram_bot(self, message, itoken, chat_id):
        bot = telebot.TeleBot(itoken)
        texto = f"{self.name} {message}"
        bot.send_message(chat_id, texto)
        return {"status": "enviado", "mensagem": texto}

    def telegram_bot_image(self, message, itoken, chat_id, path_image):
        bot = telebot.TeleBot(itoken)

        with open(path_image, 'rb') as img:
            bot.send_photo(chat_id, img)

        texto = f"{self.name} {message}"
        bot.send_message(chat_id, texto)

        return {"status": "imagem+mensagem enviada", "mensagem": texto, "imagem": path_image}

    def enviar_imagem(self, caminho_imagem, mensagem, token, chat_id):
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        with open(caminho_imagem, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': chat_id, 'caption': f"{self.name} {mensagem}"}
            requests.post(url, files=files, data=data)
