import telepot,time,random
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

	def __init__(self,id_name,name):
		self.id = id_name
		self.isBot = False
		self.name = name
		self.roles = []
		self.seed = -1
		self.spy = False
############################# bot player ###############################################
class botPlayer:

	def __init__(self,num):
		self.isBot = True
		self.name = "Bot0" + str(num)
		self.roles = []
		self.seed = -1
		self.spy = False
############################# config ###################################################
class config:

	def __init__(self,chatId,msgId):
		self.chatId = chatId
		self.msgId = msgId
		self.roles = ["Merlin"]
		self.text = ""
############################# Game class ###############################################
class game:

	def __init__(self,id_game):
		self.id = id_game
		self.state = 0
		self.totalPlayers = 0
		self.roles = []
		self.messageSetting = []
		self.players = []
		self.owner = ""
		self.history = ""
		self.mission = []
		self.needToFail = []
		self.spies = 0
		self.points = 0
		self.curr = 0
		self.consecutive = 3

	def setting(self,msg_id):
		self.messageSetting = config(self.id,msg_id)

	def getSettingIdentifier(self):
		return (self.messageSetting.chatId,self.messageSetting.msgId)

	def getSettingText(self):
		retS = "Quais destes papéis você, @" + self.owner + ", deseja adicionar?"
		retS = retS + self.messageSetting.text
		return retS

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
			self.messageSetting.text = self.messageSetting.text + "\nAdicionados:\n- Merlin\n- Assassin"
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

	def addBots(self,Q):
		for curr in range(1,Q+1):
			self.players.append(botPlayer(curr))
		self.totalPlayers = self.totalPlayers + Q

	def shuffle(self):
		pos = 0
		while pos < self.totalPlayers:
			self.players[pos].seed = random.randint(1,100)
			pos = pos + 1
		pi = 0
		while pi < self.totalPlayers:
			pj = pi + 1
			while pj < self.totalPlayers:
				if self.players[pi].seed > self.players[pj].seed:
					L = self.players[pi]
					self.players[pi] = self.players[pj]
					self.players[pj] = L
				pj = pj + 1
			pi = pi + 1

	def setRoles(self):
		cont = 0
		totalSpy = 0
		for P in self.roles:
			if P == "Palm":
				continue
			if P == "Assassin" or P == "Morgana":
				if "Palm" in self.players[cont].roles:
					cont = cont + 1
				totalSpy = totalSpy + 1
				self.players[cont].spy = True
				self.players[cont].roles.append(P)
			else:
				self.players[cont].roles.append(P)
			cont = cont + 1
		totalSpy = int(int(self.totalPlayers - 1)//2) - totalSpy 
		cont = 0
		while totalSpy > 0:
			if len(self.players[cont].roles) == 0:
				self.players[cont].spy = True
				totalSpy = totalSpy - 1
			cont = cont + 1

	def sendInfo(self,P):
		if P.isBot:
			return None
		emoji = ""
		pi = 0
		while pi < 10:
			if P.spy:
				emoji = emoji + "\U0001F534"
			else:
				emoji = emoji + "\U0001F535"
			pi = pi + 1

		if "Merlin" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é o MERLIN\n\n"+
				"Os espiões são:\n\n" + str(retorno)+"\n\n" + str(emoji))

		elif "Morgana" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é a MORGANA\n\n"+
				"Os outros espiões são:\n\n"+str(retorno)+"\n\n"+str(emoji))

		elif "Percy" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if ("Merlin" in x.roles) or ("Morgana" in x.roles):
					retorno = retorno + " - " + x.name
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é o PERCY\n\n"+
				"O Merlin é um desses jogadores:\n\n" + str(retorno)+"\n\n"+str(emoji))

		elif "Assassin" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é o ASSASSINO\n\n"+
				"Os outros espiões são:\n\n"+ str(retorno)+"\n\n"+str(emoji))

		elif P.spy:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é um ESPIÃO\n\n"+
				"Os outros espiões são:\n\n" + str(retorno)+"\n\n"+str(emoji))
		else:
			bot.sendMessage(P.id,str(emoji)+"\n\nVocê é da RESISTÊNCIA\n\n" + 
				"Ajude seu time a vencer!\n\n"+str(emoji))

	def sendAllInfo(self):
		for P in self.players:
			self.sendInfo(P)

	def printAllInfo(self):
		for P in self.players:
			print(P.name,': ',P.roles)

	def setVariables(self):
		self.spies = int(self.totalPlayers - 1)//2
		self.history = "\U000023EA    Histórico    \U000023EA\n\n"
		self.history = self.history + "Rodada 1:\n\n"
		if self.totalPlayers == 5:
			self.mission.append(2)
			self.mission.append(3)
			self.mission.append(2)
			self.mission.append(3)
			self.mission.append(3)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
		elif self.totalPlayers == 6:
			self.mission.append(2)
			self.mission.append(3)
			self.mission.append(4)
			self.mission.append(3)
			self.mission.append(4)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
		elif self.totalPlayers == 7:
			self.mission.append(2)
			self.mission.append(3)
			self.mission.append(3)
			self.mission.append(4)
			self.mission.append(4)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(2)
			self.needToFail.append(1)
		else:
			self.mission.append(3)
			self.mission.append(4)
			self.mission.append(4)
			self.mission.append(5)
			self.mission.append(5)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(1)
			self.needToFail.append(2)
			self.needToFail.append(1)
	def remember(self,to):
		text = "\U0001F4AD    Relembrando    \U0001F4AD\n\n"
		text = text + "existem " + str(self.spies) + " espiões e " + str(self.totalPlayers - self.spies)
		text = text + " resistentes\n" + "Papéis adicionais: "
		for P in self.roles:
			text = text + P + " "
		text = text + "\n\nDigite /remember para rever esta mensagem\n\nDigite /leader para visualizar a ordem dos"
		text = text + " próximos líderes das missões\n\n Digite /history para visualizar o histórico de votações"
		bot.sendMessage(to,text)
	def getHistory(self,to):
		bot.sendMessage(to,self.history)
	def leader(self,to):
		finish = self.curr + self.consecutive
		if finish >= self.totalPlayers:
			finish = finish - self.totalPlayers
		text = "\U0001F6A6    Próximos líderes    \U0001F6A6\n\n"
		pi = 0
		for L in self.players:
			text = text + "- " + L.name
			if pi == finish:
				text = text + " " + "\U000026A0"
			if pi == self.curr:
				text = text + " " + "\U0001F448"
			text = text + "\n"
			pi = pi + 1
		bot.sendMessage(to,text)


	def initGame(self):
		self.state = 1
		self.shuffle()
		if "Palm" in self.roles:
			self.players[0].roles.append("Palm")
		self.shuffle()
		self.setRoles()
		self.shuffle()
		self.sendAllInfo()
		self.printAllInfo()
		bot.sendMessage(self.id,"\U0001F534\U0001F535 Por favor, chequem seus papéis que foram"+
			" enviados no privado \U0001F534\U0001F535")
		self.setVariables()
		self.shuffle()
		self.remember(self.id)


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
			avalon.join(msg['message']['from']['id'],msg['message']['from']['username'],msg['message']['chat']['id'])
			bot.sendMessage(msg['message']['chat']['id'],"Novo jogo criado\U00002705\n\nDigite /join para entrar\n\n"
					+"Digite /leave para sair\n\nDigite /quitgame para finalizar este jogo\n\n"+
					"Digite /startgame para a diversão começar\n\n"+"Estou ativo em "+
					str(avalon.currentGames)+" grupos no momento")
			retMsg = bot.sendMessage(msg['message']['chat']['id'],
				text = "Quais destes papéis você, @" + msg['message']['from']['username'] + ", deseja adicionar?",
				reply_markup = InlineKeyboardMarkup(
					inline_keyboard = [
					[InlineKeyboardButton(text = "Merlin",callback_data = "Merlin")]
					]))
			x = avalon.findGame(msg['message']['chat']['id'])
			avalon.games[x].setting(retMsg['message_id'])
			avalon.games[x].owner = msg['message']['from']['username']
		return None
	if isRunning(msg['message']['chat']['id']) == -1:
		bot.sendMessage(msg['message']['chat']['id'],"Nenhum jogo iniciado\nDigite /newgame para iniciar um novo jogo")
		return None #break
	if '/quitgame' in msg['message']['text']:
		avalon.quit(msg['message']['chat']['id'])
		bot.sendMessage(msg['message']['chat']['id'],"Jogo finalizado.")
		return None

	x = avalon.findGame(msg['message']['chat']['id']) ## find the game

	if '/startgame' in msg['message']['text']:
		if avalon.games[x].owner != msg['message']['from']['username']:
			bot.sendMessage(msg['message']['chat']['id'],"Só @" + avalon.games[x].owner + " pode iniciar"+
				", pois ele criou a partida.")
			return None
		if avalon.games[x].state != 0:
			bot.sendMessage(msg['message']['chat']['id'],"Você já iniciou este jogo. Digite /quitgame para finalizar"+
				" o jogo atual")
			return None
		if avalon.games[x].totalPlayers < 5:
			bot.sendMessage(msg['message']['chat']['id'],'Quantidade mínima de jogadores não atingida\U0001F625'+
				"\nIrei completar com alguns bots\U0001F47E")
			avalon.games[x].addBots(5 - avalon.games[x].totalPlayers)
			avalon.games[x].initGame()
		else:
			avalon.games[x].initGame()
		return None

	if '/join' in msg['message']['text']:
		if avalon.games[x].state != 0:
			bot.sendMessage(msg['message']['chat']['id'],"Você não pode realizar esta operação, o jogo já foi iniciado.")
			return None
		flag = avalon.join(msg['message']['from']['id'],msg['message']['from']['username'],msg['message']['chat']['id'])
		if flag:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' se juntou ao game \U0000270C')
		else:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' não se preocupe, você já estava no jogo \U00002714')
		return None
	if '/leave' in msg['message']['text']:
		if avalon.games[x].state != 0:
			bot.sendMessage(msg['message']['chat']['id'],"Você não pode realizar esta operação, o jogo já foi iniciado.")
			return None
		flag = avalon.leave(msg['message']['from']['id'],msg['message']['chat']['id'])
		if flag:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' ficou com medo e saiu do jogo \U0001F61D')
			if avalon.games[x].totalPlayers == 0:
				avalon.quit(msg['message']['chat']['id'])
				bot.sendMessage(msg['message']['chat']['id'],"Por que todo mundo saiu? Jogo finalizado")
				bot.sendMessage(msg['message']['chat']['id'],"\U0001F63F")
				return None
			if msg['message']['from']['username'] == avalon.games[x].owner:
				avalon.games[x].owner = avalon.games[x].players[0].name
				bot.editMessageText(msg_identifier = avalon.games[x].getSettingIdentifier(),
						text = avalon.games[x].getSettingText(),
						reply_markup = avalon.games[x].getSettingReply())
		else:
			bot.sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' você não estava no jogo \U0001F609')
		return None
	if '/remember' in msg['message']['text'] and avalon.games[x].state != 0:
		avalon.games[x].remember(msg['message']['from']['id'])
		return None
	if '/leader' in msg['message']['text'] and avalon.games[x].state != 0:
		avalon.games[x].leader(msg['message']['from']['id'])
		return None
	if '/history' in msg['message']['text'] and avalon.games[x].state != 0:
		avalon.games[x].getHistory(msg['message']['from']['id'])
		return None


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
		if x != -1:
			if avalon.games[x].state == 0 and msg['callback_query']['message']['message_id'] == avalon.games[x].messageSetting.msgId:
				if msg['callback_query']['from']['username'] == avalon.games[x].owner:
					avalon.games[x].settingUpdate(msg['callback_query']['data'])
					bot.editMessageText(msg_identifier = avalon.games[x].getSettingIdentifier(),
						text = avalon.games[x].getSettingText(),
						reply_markup = avalon.games[x].getSettingReply())
