# Copyright (C) 2020-2021 by BukanDev@Github, < https://github.com/BukanDev >.
#
# This file is part of < https://github.com/BukanDev/TikTokDL > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/BukanDev/TikTokDL/blob/main/LICENSE >
# @pySmartDL
#
# All rights reserved.


import os
import telebot
from telebot import types
import requests

TOKEN = os.environ.get('TOKEN', '5444155072:AAEnO2c6esaOqI-QJurxfG9Oym1DDZeZHNg')

bot = telebot.TeleBot(TOKEN)
me = bot.get_me()
print(f'Bot telah aktif @{me.username}')


@bot.message_handler(commands=['start', 'help'])
def start_message(m):
	bot.send_message(m.chat.id, '*Selamat datang saya adalah bot untuk mengunduh video dari tiktok*\n\n*Caranya :* _Tinggal kirimkan saja link tiktok ke bot ini dan nanti anda kan di kirimkan video sesuai link_', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def tiktokdl(m):
    if m.text.startswith(('https://www.tiktok.com', 'http://www.tiktok.com', 'https://vm.tiktok.com', 'https://vt.tiktok.com')):
        try:
            bot.send_message(m.chat.id, 'Processing...')
            url = requests.get(f'https://api.douyin.wtf/api?url={m.text}').json()
            video = url['nwm_video_url']
            audio = url['video_music_url']
            videotitle = url['video_title']
            videomusictitle = url['video_music_title']
            autor = url['video_author_nickname']
            time = url['analyze_time']
            bot.send_video(m.chat.id, video, caption=f'*INFORMATION:*\n\n*- Video title:* {videotitle}\n*- Audio:* {videomusictitle}\n*- Author Nickname:* {autor}\n\n*Total parsing time:* {time} seconds', parse_mode='Markdown')
            bot.send_audio(m.chat.id, audio)
            
        except Exception as e:
            print(e)
            bot.send_message(m.chat.id, f'Sepertinya link yang kamu masukkan salah')
        
bot.polling()
