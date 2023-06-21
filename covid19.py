import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1045278072:AAEcu7E77CtFCfjd77xpxDYFShUyhaREkZI')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Во всём мире')
	btn2 = types.KeyboardButton('Англия')
	btn3 = types.KeyboardButton('Россия')
	btn4 = types.KeyboardButton('Румыния')
	btn5 = types.KeyboardButton('Молдова')
	markup.add(btn1, btn2, btn3, btn4, btn5)

send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавирус напишите " \
	f"название страны, например: США, Украина, Россия и так далее\n\nЗаходи к нам на сайт <a href='https://itproger.com'>itProger</a>"
	bot. send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "Англия":
		location = covid19.getLocationByCountryCode("UK")
	elif get_message_bot == "Украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "Россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "Румыния":
		location = covid19.getLocationByCountryCode("ROM")
	elif get_message_bot == "Молдова":
		location = covid19.getLocationByCountryCode("MD")
	elif get_message_bot == "Италия":
		location = covid19.getLocationByCountryCode("IT")
	
	else:
		location = covid19.getLatest()
	final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)