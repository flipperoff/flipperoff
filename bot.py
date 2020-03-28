import telebot
import config
from bs4 import BeautifulSoup
import requests as req
from itertools import groupby
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def get_mainnews():
	resp = req.get("https://gordonua.com/")
 
	soup = BeautifulSoup(resp.text, 'lxml')

	body = soup.body
	li = body.find('div',class_ = "tab-content").find_all("li")
	a = []
	for i in li:
		a.append(i.find('a'))
	links = ([link['href'] for link in a if link.has_attr('href')])
	text = []
	for i in a:
		text.append(i.text)
	for i in range(len(text)):
		text[i] = ''.join(text[i].split('\n'))
	news_ = {}
	for i in range(len(text)):
		news_[text[i]]=links[i]

	return text,news_

def get_sport():
	resp = req.get("https://gordonua.com/news/sport.html")
 
	soup = BeautifulSoup(resp.text, 'lxml')

	body = soup.body
	lenta = body.find_all("div", class_="lenta sw34_20")
	media = body.find("div",class_="lenta sw34_20").find_all("div",class_="media")
	lenta_head = []
	for i in media:
		lenta_head.append(i.find('div',class_ = "lenta_head"))
	a = []
	for i in lenta_head:
		a.append(i.find("a"))
	links = ([link['href'] for link in a if link.has_attr('href')])
	text = []
	for i in a:
		text.append(i.text)
	for i in range(len(text)):
		text[i] = ''.join(text[i].split('\n'))
	news_ = {}
	for i in range(len(text)):
		news_[text[i]]=links[i]

	return text,news_ 

def get_politics():
	resp = req.get("https://gordonua.com/news/politics.html")
 
	soup = BeautifulSoup(resp.text, 'lxml')

	body = soup.body
	lenta = body.find_all("div", class_="lenta sw34_20")
	media = body.find("div",class_="lenta sw34_20").find_all("div",class_="media")
	lenta_head = []
	for i in media:
		lenta_head.append(i.find('div',class_ = "lenta_head"))
	a = []
	for i in lenta_head:
		a.append(i.find("a"))
	links = ([link['href'] for link in a if link.has_attr('href')])
	text = []
	for i in a:
		text.append(i.text)
	for i in range(len(text)):
		text[i] = ''.join(text[i].split('\n'))
	news_ = {}
	for i in range(len(text)):
		news_[text[i]]=links[i]

	return text,news_

def get_war():
	resp = req.get("https://gordonua.com/news/war.html")
 
	soup = BeautifulSoup(resp.text, 'lxml')

	body = soup.body
	lenta = body.find_all("div", class_="lenta sw34_20")
	media = body.find("div",class_="lenta sw34_20").find_all("div",class_="media")
	lenta_head = []
	for i in media:
		lenta_head.append(i.find('div',class_ = "lenta_head"))
	a = []
	for i in lenta_head:
		a.append(i.find("a"))
	links = ([link['href'] for link in a if link.has_attr('href')])
	text = []
	for i in a:
		text.append(i.text)
	for i in range(len(text)):
		text[i] = ''.join(text[i].split('\n'))
	news_ = {}
	for i in range(len(text)):
		news_[text[i]]=links[i]

	return text,news_ 

def get_kyiv():
	resp = req.get("https://gordonua.com/news/kiev.html")
 
	soup = BeautifulSoup(resp.text, 'lxml')

	body = soup.body
	lenta = body.find_all("div", class_="lenta sw34_20")
	media = body.find("div",class_="lenta sw34_20").find_all("div",class_="media")
	lenta_head = []
	for i in media:
		lenta_head.append(i.find('div',class_ = "lenta_head"))
	a = []
	for i in lenta_head:
		a.append(i.find("a"))
	links = ([link['href'] for link in a if link.has_attr('href')])
	text = []
	for i in a:
		text.append(i.text)
	for i in range(len(text)):
		text[i] = ''.join(text[i].split('\n'))
	news_ = {}
	for i in range(len(text)):
		news_[text[i]]=links[i]

	return text,news_ 

@bot.message_handler(commands=['start'])
def welcome(message):
	photo = open('logo.png','rb')
	bot.send_photo(message.chat.id, photo)
	markup = types.InlineKeyboardMarkup()
	item1 = types.InlineKeyboardButton("Киев",callback_data="kyiv")
	item2 = types.InlineKeyboardButton("Война в Украине", callback_data='war')
	item3 = types.InlineKeyboardButton("Политика", callback_data='politics')
	item4 = types.InlineKeyboardButton("Спорт",callback_data='sport')
	item5 = types.InlineKeyboardButton("Последние новости",callback_data = 'mainnews')
	markup.add(item1,item2,item3,item4,item5)
	



	bot.send_message(message.chat.id, 'welcome, {0.first_name}!\n Here are Gordon news!'.format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)

@bot.message_handler(content_types=['text'])
def reply(message):
	pass
	

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	
	if call.data == "kyiv":
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton(str(text[0]),callback_data="kyiv.0")
		item2 = types.InlineKeyboardButton(str(text[1]),callback_data = 'kyiv.1')
		item3 = types.InlineKeyboardButton(str(text[2]),callback_data = 'kyiv.2')
		item4 = types.InlineKeyboardButton(str(text[3]),callback_data = 'kyiv.3')
		item5 = types.InlineKeyboardButton(str(text[4]),callback_data = 'kyiv.4')
		item6 = types.InlineKeyboardButton("Главная",callback_data = 'main')
		markup.add(item1,item2,item3,item4,item5,item6)

		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Киев",reply_markup = markup)
	elif call.data == 'kyiv.0':
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[0]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[0])),reply_markup = markup)
	elif call.data == 'kyiv.1':
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[1]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[1])),reply_markup = markup)
	elif call.data == 'kyiv.2':
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[2]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[2])),reply_markup = markup)
	elif call.data == 'kyiv.3':
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[3]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[3])),reply_markup = markup)
	elif call.data == 'kyiv.4':
		text,news_ = get_kyiv()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[4]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[4])),reply_markup = markup)
	

	elif call.data == "Назад":
		bot.delete_message(call.message.chat.id, call.message.message_id)
	

	elif call.data == "main":
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Киев",callback_data="kyiv")
		item2 = types.InlineKeyboardButton("Война в Украине", callback_data='war')
		item3 = types.InlineKeyboardButton("Политика", callback_data='politics')
		item4 = types.InlineKeyboardButton("Спорт",callback_data = 'sport')
		item5 = types.InlineKeyboardButton("Последние новости",callback_data = 'mainnews')
		markup.add(item1,item2,item3,item4,item5)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Here are Gordon news!",reply_markup = markup)
	

	elif call.data == 'war':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton(str(text[0]),callback_data="war.0")
		item2 = types.InlineKeyboardButton(str(text[1]),callback_data = 'war.1')
		item3 = types.InlineKeyboardButton(str(text[2]),callback_data = 'war.2')
		item4 = types.InlineKeyboardButton(str(text[3]),callback_data = 'war.3')
		item5 = types.InlineKeyboardButton(str(text[4]),callback_data = 'war.4')
		item6 = types.InlineKeyboardButton("Главная",callback_data = 'main')
		markup.add(item1,item2,item3,item4,item5,item6)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Война в Украине",reply_markup = markup)
	elif call.data == 'war.0':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[0]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[0])),reply_markup = markup)
	elif call.data == 'war.1':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[1]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[1])),reply_markup = markup)
	elif call.data == 'war.2':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[2]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[2])),reply_markup = markup)
	elif call.data == 'war.3':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[3]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[3])),reply_markup = markup)
	elif call.data == 'war.4':
		text,news_ = get_war()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[4]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[4])),reply_markup = markup)
	


	elif call.data == 'politics':
		text,news_ = get_politics()
		markup = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton(str(text[0]),callback_data="politics.0")
		item2 = types.InlineKeyboardButton(str(text[1]),callback_data = 'politics.1')
		item6 = types.InlineKeyboardButton("Главная",callback_data = 'main')
		markup.add(item1,item2,item6)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Война в Украине",reply_markup = markup)
	elif call.data == 'politics.0':
		text,news_ = get_politics()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[0]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[0])),reply_markup = markup)
	elif call.data == 'politics.1':
		text,news_ = get_politics()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[1]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[1])),reply_markup = markup)
	

	elif call.data == 'sport':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton(str(text[0]),callback_data="sport.0")
		item2 = types.InlineKeyboardButton(str(text[1]),callback_data = 'sport.1')
		item3 = types.InlineKeyboardButton(str(text[2]),callback_data = 'sport.2')
		item4 = types.InlineKeyboardButton(str(text[3]),callback_data = 'sport.3')
		item5 = types.InlineKeyboardButton(str(text[4]),callback_data = 'sport.4')
		item6 = types.InlineKeyboardButton("Главная",callback_data = 'main')
		markup.add(item1,item2,item3,item4,item5,item6)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Война в Украине",reply_markup = markup)
	elif call.data == 'sport.0':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[0]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[0])),reply_markup = markup)
	elif call.data == 'sport.1':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[1]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[1])),reply_markup = markup)
	elif call.data == 'sport.2':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[2]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[2])),reply_markup = markup)
	elif call.data == 'sport.3':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[3]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[3])),reply_markup = markup)
	elif call.data == 'sport.4':
		text,news_ = get_sport()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[4]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[4])),reply_markup = markup)
	
	elif call.data == 'mainnews':
		text,news_ = get_mainnews()
		markup = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton(str(text[0]),callback_data="mainnews.0")
		item2 = types.InlineKeyboardButton(str(text[1]),callback_data = 'mainnews.1')
		item3 = types.InlineKeyboardButton(str(text[2]),callback_data = 'mainnews.2')
		item4 = types.InlineKeyboardButton(str(text[3]),callback_data = 'mainnews.3')
		item5 = types.InlineKeyboardButton(str(text[4]),callback_data = 'mainnews.4')
		item6 = types.InlineKeyboardButton("Главная",callback_data = 'main')
		markup.add(item1,item2,item3,item4,item5,item6)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Последние новости",reply_markup = markup)
	elif call.data == 'mainnews.0':
		text,news_ = get_mainnews()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[0]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[0])),reply_markup = markup)
	elif call.data == 'mainnews.1':
		text,news_ = get_mainnews()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[1]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[1])),reply_markup = markup)
	elif call.data == 'mainnews.2':
		text,news_ = get_mainnews()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[2]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[2])),reply_markup = markup)
	elif call.data == 'mainnews.3':
		text,news_ = get_mainnews()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[3]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[3])),reply_markup = markup)
	elif call.data == 'mainnews.4':
		text,news_ = get_mainnews 	()
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton("Назад", callback_data = "Назад")
		markup.add(item1)
		bot.send_message(call.message.chat.id, str(text[4]) + "\nhttps://gordonua.com/news/kiev" + str(news_.get(text[4])),reply_markup = markup)
	else:
		bot.send_message(call.message.chat.id, "Not")
		
bot.polling(none_stop=True)
