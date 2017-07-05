from __future__ import print_function
import jsonlines
import pprint
o = {}
def BuscaPorNome():
    nome = str(raw_input('Digite o Nome Da Carta: ')).lower()
    with jsonlines.open("gwent.jsonl") as reader:
    	for obj in reader:
    		if(obj['name'].lower() == nome):
    			pprint.pprint(obj)
def MostrarCartas():
	with jsonlines.open('gwent.jsonl') as r:
		for item in r:
			print(item['name'],end =" | ")
def mostrarFactions():
	print('''Digite:
	1-PARA MONSTROS
	2-PARA NEUTRAS
	3-PARA REINO DO NORTE 
	4-PARA SCOIA'TAEL
	5-PARA NILFGAARD
		''')
	i = int(raw_input())
	if(i == 1):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['faction'] == 'Monsters'):
					print(item['name'])
	elif(i==2):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['faction'] == 'Neutral'):
					print(item['name'])
	elif(i==3):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['faction'] == 'Northern Realms'):
					print(item['name'])
	elif(i ==4):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['faction'] == "Scoia'tael"):
					print(item['name'])
	else:
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['faction'] == "Nilfgaard"):
					print(item['name'])
def mostrarType():
	print('''Digite:
	1-PARA CARTAS ESPECIAS
	2-PARA UNIDADES
		''')
	i = int(raw_input())
	if(i == 1):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if('categories' in item and"Special" in item['categories']):
					print(item['name'])
	else:
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(not 'categories' in item or not "Special" in item['categories']):
					print(item['name'])
def mostrarCor():
	print('''Digite:
	1-PARA OURO
	2-PARA PRATA
	3-PARA BRONZE
		''')
	i = int(raw_input())
	if(i == 1):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['type']== 'Gold'):
					print(item['name'])
	elif(i == 2):
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['type'] == 'Silver'):
					print(item['name'])
	else:
		with jsonlines.open('gwent.jsonl') as r:
			for item in r:
				if(item['type'] == 'Bronze'):
					print(item['name'])