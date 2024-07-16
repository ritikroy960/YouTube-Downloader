from flask import Flask
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
  app.run(debug=True)

token = '7234737115:AAHtK02uy5rFJxICyffdqc2ZRtF13aQEuCA'

bot = telebot.TeleBot(token)

@bot.message_handler(['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Hii {name}\n I'm YouTube Downloader Bot. Send me a YouTube video link and I'll download it for you.", reply_markup=InlineKeyboardMarkup(start_button))

start_button = [[
  InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/devx_coder"),
    InlineKeyboardButton("DEVELOPER", url="https://replit.com/@priyanshu999")
]]

@bot.message_handler(['video'])
def video(message):
    try:
        url = message.text.split(' ', 1)[1]
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        bot.reply_to(message, video.url)

    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred while downloading the video")

@bot.message_handler(['audio'])
def audio(message):
    try:
        url = message.text.split(' ', 1)[1]
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        bot.reply_to(message, audio.url)

    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred while downloading the audio.")

@bot.message_handler()
def send(message):
    bot.reply_to(message, "Please Send Link in This Format\n /video https://example.com\n /audio https://example.com")

bot.polling()