#RODANDO EM PYTHON 2.7,12
import telegram
import ConfigParser
import requests
import json
import redis
from telegram.ext import Updater


#Setando BOT apartir de INI
config = ConfigParser.ConfigParser()
config.read('config.ini')

#Pegando TOKEN BOT TELEGRAM
TKB = config.get('DEFAULT','token')

#UNINDO URL BOT + TOKEN
url = 'https://api.telegram.org/bot' + TKB

#CONECTANDO API TELGRAM
#UPDATE RECEBE MENSAGEM
#DISPATCHER RECEBE COMANDOS
updater = Updater(token = TKB)
dispatcher = updater.dispatcher

#CONECTANDO AO SERVIDO REDIS EASY PEASY
BD = redis.StrictRedis(host = config.get('DB','host'),
					   port = config.getint('DB', 'port'),
					   db = config.getint('DB', 'db'))


getME = requests.get(url+'/getMe')
if(getME.status_code == 200 ):
	bot = json.loads(getME.content.decode('latin1'))
print bot['result']['first_name']
nome = bot['result']['first_name'].lower()
card = requests.get('https://gwent-api.herokuapp.com/card/name/'+nome+'/flavor')
if(card.status_code == 200):
	print card.content
