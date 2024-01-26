import os
import telebot
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot=telebot.TeleBot(BOT_TOKEN)

'''@bot.message_handler(commands=['start', 'hello'])
def sned_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
  bot.reply_to(message, message.text)'''




@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
  text = "Whats your zodiac sign?\nChoose one: *Aeries*, *Taurus*, *Gemini*, *Cancer*, *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, *Pisces*."
  sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
  bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
  sign = message.text
  text = "What day do you want to know?\nchoose one: *Today*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
  sent_msg = bot.send_message(
    message.chat.id, text, parse_mode="Markdown")
  bot.register_next_step_handler(
    sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign):
  day = message.text
  horoscope = get_daily_horoscope(sign, day)
  data = horoscope["data"]
  horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
  bot.send_message(message.chat.id, "Here's your horoscope!")
  bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


def get_daily_horoscope(sign: str, day: str) -> dict:
  url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
  params = {"sign": sign, "day": day}
  response = requests.get(url, params)

  return response.json()







print("Bot is Starting......")
bot.infinity_polling()
