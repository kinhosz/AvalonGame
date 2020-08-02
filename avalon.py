import telepot,time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

bot = telepot.Bot('1331608627:AAFgtfQqyP6d-hA8yUy2aMkEw4dgzC0ULGg')

##########init##########
old_id = 0
x = bot.getUpdates()
for m in x:
	old_id = m['update_id']

old_id = old_id + 1

########## txt ##########################################################################
welcomeTXT = '\U00002764 Olá, seja bem-vindo ao Avalon Game \U00002764\n\n'
welcomeTXT = welcomeTXT + 'Para jogar, me adicione em algum grupo e envie o comando /newgame.\n\n'
welcomeTXT = welcomeTXT + '/help \U000027a1 obter ajuda sobre a mecânica do jogo\n'
welcomeTXT = welcomeTXT + '/about \U000027a1 mais informações sobre mim e meu criador\n'
welcomeTXT = welcomeTXT + '/list \U000027a1 liste todos os comandos deste bot\n'

helpTXT = "depois eu digito o help aqui"
listTXT = "depois eu digito os comandos aqui"
aboutTXT = "depois digito o about"
################## flip message ########################################################
def receiveMessage():
	global old_id
	while 1:
		upd = bot.getUpdates(offset = old_id)
		if len(upd) != 0:
			old_id = upd[0]['update_id']
			old_id = old_id + 1
			break
	return upd[0] 
############################# player class #############################################
class player:

	def __init__(self,id,name):
		self.id = id
		self.name = name
		self.roles = []
############################# config ###################################################
class config:

	def __init__(self,chatId,msgId,text):
		self.chatId = chatId
		self.msgId = msgId
		self.roles = ["Merlin"]
		self.text = text
############################# Game class ###############################################
class game:

	def __init__(self,id):
		self.id = id
		self.state = 0
		self.totalPlayers = 0
		self.roles = []
		self.messageSetting = []
		self.players = []
		self.owner = ""

	def setting(self,msg_id,text):
		self.messageSetting = config(self.id,msg_id,text)

	def getSettingIdentifier(self):
		return (self.messageSetting.chatId,self.messageSetting.msgId)

	def getSettingText(self):
		return self.messageSetting.text

	def getSettingReply(self):
		L = []
		for R in self.messageSetting.roles:
			row = []
			row.append(InlineKeyboardButton(text = R,callback_data = R))
			L.append(row)
		obj = InlineKeyboardMarkup(inline_keyboard = L)
		return obj

	def settingUpdate(self,data):
		self.messageSetting.roles.remove(data)
		if data == 'Merlin':
			self.messageSetting.text = self.messageSetting.text + "\nAdicionados:\n- Merlin\n- Assassino"
			self.messageSetting.roles.append("Percy")
			self.messageSetting.roles.append("Palm")
			self.roles.append("Merlin")
			self.roles.append("Assassin")

		if data == 'Percy':
			self.messageSetting.text = self.messageSetting.text + "\n- Percy"
			self.messageSetting.roles.append("Morgana")
			self.roles.append("Percy")

		if data == 'Morgana':
			self.messageSetting.text = self.messageSetting.text + "\n- Morgana"
			self.roles.append("Morgana")

		if data == 'Palm':
			self.messageSetting.text = self.messageSetting.text + "\n- Palm"
			self.roles.append("Palm")

############################# General Class ############################################
class general:

	def __init__(self):
		self.currentGames = 0
		self.games = []

	def quit(self,id):
		cont = 0
		for G in self.games:
			if G.id != id:
				cont = cont + 1
			else:
				break
		self.games.pop(cont)
		self.currentGames = self.currentGames - 1

	def newgame(self,id):
		self.currentGames = self.currentGames + 1
		self.games.append(game(id))

	def gamesEnable(self):
		return self.currentGames

	def findChatEnable(self,chat):
		for G in self.games:
			if chat == G.id:
				return True
		return False
	def findGame(self,id):
		pos = 0
		for G in self.games:
			if G.id == id:
				return pos
			pos = pos + 1
		return -1
	def join(self,id_player,name_player,chat):
		pos = 0
		while pos < self.currentGames:
			if self.games[pos].id == chat:
				for P in self.games[pos].players:
					if P.id == id_player:
						return False
				self.games[pos].players.append(player(id_player,name_player))
				self.games[pos].totalPlayers = self.games[pos].totalPlayers + 1
				return True
			pos = pos + 1
		return False
	def leave(self,id_player,chat):
		pos = 0
		while pos < self.currentGames:
			if self.games[pos].id == chat:
				j = 0
				while j < self.games[pos].totalPlayers:
					if self.games[pos].players[j].id == id_player:
						self.games[pos].players.pop(j)
						self.games[pos].totalPlayers = self.games[pos].totalPlayers - 1
						return True
					j = j + 1
			pos = pos + 1
		return False


######################## is running ###################################################
def isRunning(chat):
	global avalon
	return avalon.findGame(chat)


####### some global variables ##########################################################
sentMessage = None
avalon = general()

############################### private mode ##########################################
def privateMode(msg):
	
	if '/start' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],welcomeTXT)
	if '/newgame' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],"Este comando só funciona em grupos ou supergrupos \U0000274C")
	if '/help' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],helpTXT)
	if '/about' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],aboutTXT)
	if '/list' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],listTXT)

############################## group mode #############################################
def groupMode(msg):
	global avalon

	if '/newgame' in msg['message']['text']:
		if isRunning(msg['message']['chat']['id']) != -1:
			bot.sendMessage(msg['message']['chat']['id'],'Um jogo já foi iniciado. Digite /join para entrar ou /quitgame para finalizar o jogo atual')
		else:
			avalon.newgame(msg['message']['chat']['id'])
			bot.sendMessage(msg['message']['chat']['id'],"Novo jogo criado\U00002705\n\nDigite /join para entrar\n\n"
					+"Digite /leave para sair\n\nDigite /quitgame para finalizar este jogo\n\n"+
					"Digite /startgame para a diversão começar\n\n"+"Estou ativo em "+
					str(avalon.currentGames)+" grupos no momento")
			strNG = "Quais destes papeis você @" + msg['message']['from']['username']+" deseja adicionar ao jogo?"
			retMsg = bot.sendMessage(msg['message']['chat']['id'],text = strNG,
				reply_markup = InlineKeyboardMarkup(
					inline_keyboard = [
					[InlineKeyboardButton(text = "Merlin",callback_data = "Merlin")]
					]))
			x = avalon.findGame(msg['message']['chat']['id'])
			avalon.games[x].setting(retMsg['message_id'],strNG)
			avalon.games[x].owner = msg['message']['from']['username']
	if isRunning(msg['message']['chat']['id']) == -1:
		bot.sendMessage(msg['message']['chat']['id'],"Nenhum jogo iniciado. Digite /newgame para iniciar um novo jogo")
		return None #break
	if '/quitgame' in msg['message']['text']:
		avalon.quit(msg['message']['chat']['id'])
		bot.sendMessage(msg['message']['chat']['id'],"Jogo finalizado.")
	if '/join' in msg['message']['text']:
		flag = avalon.join(msg['message']['from']['id'],msg['message']['from']['username'],msg['message']['chat']['id'])
		if flag:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' se juntou ao game \U0000270C')
		else:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' não se preocupe, você já estava no jogo \U00002714')
	if '/leave' in msg['message']['text']:
		flag = avalon.leave(msg['message']['from']['id'],msg['message']['chat']['id'])
		if flag:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' ficou com medo e saiu do jogo \U0001F61D')
		else:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' você não estava no jogo \U0001F609')
	if '/startgame' in msg['message']['text']:
		x = avalon.findGame(msg['message']['chat']['id'])
		if avalon.games[x].totalPlayers < 5:
			bot.sendMessage(msg['message']['chat']['id'],'Quantidade mínima de jogadores não atingida\U0001F625')
		else:
			bot.sendMessage(msg['message']['chat']['id'],"daqui a pouco codo essa parte")


######### main #################################################################
while 1:
	msg = receiveMessage()
	if 'message' in  msg:
		if 'text' in msg['message']:
			print(msg['message']['from']['username'],': ',msg['message']['text'])
			if 'private' == msg['message']['chat']['type']:
				privateMode(msg)
			else:
				groupMode(msg)
	elif 'callback_query' in msg:
		x = avalon.findGame(msg['callback_query']['message']['chat']['id'])
		if msg['callback_query']['from']['username'] == avalon.games[x].owner:
			avalon.games[x].settingUpdate(msg['callback_query']['data'])
			bot.editMessageText(msg_identifier = avalon.games[x].getSettingIdentifier(),
				text = avalon.games[x].getSettingText(),
				reply_markup = avalon.games[x].getSettingReply())
