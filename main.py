#RODANDO EM PYTHON 2.7.12
import telegram
import ConfigParser
import requests
import json
import CardFunctions as gs
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters


#Setando BOT apartir de INI
config = ConfigParser.ConfigParser()
config.read('config.ini')

#Pegando TOKEN BOT TELEGRAM
TKB = config.get('DEFAULT','token')

#UNINDO URL BOT + TOKEN
url = 'https://api.telegram.org/bot' + TKB


#CONECTANDO AO SERVIDO REDIS EASY PEASY
#BD = redis.StrictRedis(host = config.get('DB','host'),
#					   port = config.getint('DB', 'port'),
#					   db = config.getint('DB', 'db'))

#FUNCÇÃO QUE INICIA O BOT COM /START
def start(bot, update):
	update.message.reply_text("O QUE VOCE QUER HUMANO ?")

#FUNCAO DE COMANDO /AJUDA
def ajuda (bot, update):
	update.message.reply_text("QUER AJUDA MORTAL ? PERGUNTA PRO ORACULO GOOGLE.COM !")
#FUNCAO QUE RETORNA TEXTO PRO USUARIO
def escre(bot, update):
	update.message.reply_text(update.message_text)

getME = requests.get(url+'/getMe')
if(getME.status_code == 200 ):
	bot = json.loads(getME.content.decode('latin1'))
	print bot['result']['first_name']
	nome = bot['result']['first_name'].lower()
	card = requests.get('https://gwent-api.herokuapp.com/card/name/'+nome+'/flavor')
	if(card.status_code == 200):
		print card.content


def main():
#CONECTANDO API TELGRAM
#UPDATE RECEBE MENSAGEM
#DISPATCHER RECEBE COMANDOS
	updater = Updater(token = TKB)
	dispatcher = updater.dispatcher

#CRIANDO OS HANDLERS DE CADA COMANDO DO USUARIO
	dispatcher.add_handler(CommandHandler("start",start))
	dispatcher.add_handler(CommandHandler("ajuda", ajuda))

#CASO O USUSARIO NAO DIGITE NENHUM DESSES COMANDOS ELE SOMENTE RETORNA O QUE ELE DISSE
	dispatcher.add_handler(MessageHandler([Filters.text], escre))
#COMANDO QUE FAZ O BOT FAZER UPDATE.
	updater.start_polling()
	updater.idle()
#GABIARRA DE POO PRA RODAR O MAIN !! xD
if __name__ == '__main__':
	main()
