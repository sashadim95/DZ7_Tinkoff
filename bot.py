import telebot
from yandex_translate import YandexTranslate

bot = telebot.TeleBot("my_token")
translate = YandexTranslate('traslate_token')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Привет! Я повторюшка дядя хрюшка со знанием анлгийского')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, translate.translate(message.text, 'en').get('text')[0])

@bot.message_handler(content_types=['document', 'audio', 'voice', 'photo'])
def handle_document_audio(message):
    bot.send_message(message.chat.id, 'Я работаю только с текстом')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

if __name__ == '__main__':
     bot.polling(none_stop=True)
