import telegram
import ConfigParser
import requests
import json
#Setando BOT apartir de INI

config = ConfigParser.ConfigParser()
config.read('config.ini')
TKB = config.get('DEFAULT','token')
url = 'https://api.telegram.org/bot' + TKB
getME = requests.get(url+'/getMe')
if(getME.status_code == 200 ):
	bot = json.loads(getME.content.decode('latin1'))
print bot['result']['first_name']
nome = bot['result']['first_name'].lower()
card = requests.get('https://gwent-api.herokuapp.com/card/name/'+nome+'/flavor')
if(card.status_code == 200):
	print card.content