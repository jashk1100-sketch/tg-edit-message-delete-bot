import telebot
import os

TOKEN = os.environ.get("8544744508:AAECE2NXcvOrbDVFlMmkUCKjNlaN8FcZaEM")
bot = telebot.TeleBot(TOKEN)

WARNING = "❌ Edited messages are not allowed in this group!"

@bot.edited_message_handler(func=lambda m: True)
def delete_edited(m):
    try:
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, WARNING)
    except:
        pass

print("Bot is running...")
bot.infinity_polling()
