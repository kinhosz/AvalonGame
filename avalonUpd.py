import telepot,time,random
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

bot = telepot.Bot('Your token here')

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

helpTXT = "Avalon é uma vertente do jogo THE RESISTANCE. Os jogadores são dividos em dois grupos: resistentes e espiões."
helpTXT = helpTXT + " Os resistentes estão tentando derrubar o governo, espiões são os infiltrados do governo colocados"
helpTXT = helpTXT + " com o objetivo de desestabilizar o grupo. O objetivo do jogo é descobrir quem são os espiões por meio das"
helpTXT = helpTXT + " missões.\n\nMissões \U000027a1 O jogo é composto por 5 missões no total, a cada rodada um líder é responsável por"
helpTXT = helpTXT + " escolher um grupo de pessoas (com ele incluso, ou não) para ir à missão. Este grupo passa por uma votação,"
helpTXT = helpTXT + " a maioria dos jogadores deve votar se aprova ou não o time escolhido. Se não for aprovado, o líder é trocado"
helpTXT = helpTXT + " e é montado um novo time. Se acontecer 4 rejeições seguidas os espiões recebem 1 ponto. Se o time for aprovado"
helpTXT = helpTXT + " então apenas eles participam de uma votação para sabotar ou não a missão. A resistência nunca pode sabotar uma missão."
helpTXT = helpTXT + " Se a missão possuir a quantidade suficiente de votos para ser sabotada, então ela é, caso contrário, a missão"
helpTXT = helpTXT + " passa com sucesso e a resistência ganha 1 ponto. Vence o grupo que marcar 3 pontos primeiro."
helpTXT = helpTXT + "\n\nDetalhes \U000027a1 Os espiões conhecem todos os outros espiões. Os resistentes não possuem nenhuma informação"
helpTXT = helpTXT + " inicial sobre os outros jogadores.\n\nAlguns papéis adicionais deixam o jogo mais emocionante. Digite /roles"
helpTXT = helpTXT + " para visualizar os papéis disponíveis.\nhttps://pt.wikipedia.org/wiki/Resist%C3%AAncia_(jogo)"

listTXT = "Estes são todos os comandos deste bot\n\nModo Privado:\n\n"
listTXT = listTXT + "/help \U000027a1 Entenda como o jogo funciona\n"
listTXT = listTXT + "/about \U000027a1 Veja mais informações sobre este bot e sobre o responsável por criar o código\n"
listTXT = listTXT + "/roles \U000027a1 Entenda quais são os papéis disponíveis e quais são suas ações no jogo\n"
listTXT = listTXT + "/start \U000027a1 Inicie o bot no chat privado\n"
listTXT = listTXT + "/list \U000027a1 veja todos os comandos disponíveis\n"
listTXT = listTXT + "\nModo Público (grupos ou supergrupos):\n\n"
listTXT = listTXT + "/newgame \U000027a1 inicie um novo jogo\n"
listTXT = listTXT + "/quitgame \U000027a1 feche o jogo atual\n"
listTXT = listTXT + "/join \U000027a1 Entre no jogo aberto recentemente\n"
listTXT = listTXT + "/leave \U000027a1 saia do jogo aberto recentemente\n"
listTXT = listTXT + "/remember \U000027a1 reveja as configurações do jogo aberto\n"
listTXT = listTXT + "/leader \U000027a1 veja a sequência dos líderes das missões\n"
listTXT = listTXT + "/history \U000027a1 veja o histórico de votações do jogo atual\n"

aboutTXT = "Olá, obrigado por usar meu bot !!\n\nCaso você encontre algum bug, deseja fazer críticas ou queira sugerir melhorias, entre em"
aboutTXT = aboutTXT + " contato com meu canal direto no telegram: @kinhosz\n\nEste é um projeto open source, visite meu repositório em"
aboutTXT = aboutTXT + " (https://github.com/kinhosz/AvalonGame), siga e deixe seu gostei para me incentivar a realizar mais projetos deste tipo\U00002764"

rolesTXT = "Papéis adicionais\n\n"
rolesTXT = rolesTXT + "Merlin \U000027a1 É da resistência. Ao iniciar o jogo ele recebe informações adicionais sobre quem são os"
rolesTXT = rolesTXT + " espiões. Cuidado: O Merlin não pode ser descoberto, pois, se a resistência ganhar, o assassino pode tentar"
rolesTXT = rolesTXT + " matá-lo e reverter a vitória para os espiões. Ao ser adicionado, o assassino também será automaticamente."
rolesTXT = rolesTXT + "\n\nDesbloqueado por: Nenhum jogador.\nDesbloqueia: Percy e Palm\n"
rolesTXT = rolesTXT + "---------------------------------------------------------------\n"
rolesTXT = rolesTXT + "Assassino \U000027a1 É espião. Ao final do jogo, se a resistência vencer, o assassino recebe a chance de tentar"
rolesTXT = rolesTXT + " matar o Merlin. Se conseguir, vitória dos espiões, caso contrário, a vitória é da resistência\n"
rolesTXT = rolesTXT + "---------------------------------------------------------------\n"
rolesTXT = rolesTXT + "Percy \U000027a1 É da resistência. No início do jogo ele recebe a informação sobre quem é o Merlin, mas, se a"
rolesTXT = rolesTXT + " Morgana for adicionada, ele recebe dois nomes: um para a Morgana e o outro para o Merlin. Mas ele precisa descobrir"
rolesTXT = rolesTXT + " quem é quem.\n\nDesbloqueado por: Merlin\nDesbloqueia: Morgana\n"
rolesTXT = rolesTXT + "---------------------------------------------------------------\n"
rolesTXT = rolesTXT + "Palm \U000027a1 É da resistência. O jogador que recebe o Palm como um dos papéis nunca saberá até terminar o"
rolesTXT = rolesTXT + " jogo. O Palm aparece como espião para o Merlin e para os outros espiões, mas joga como resistência\n"
rolesTXT = rolesTXT + "\nDesbloqueado por: Merlin\nDesbloqueia: Ninguém\n"
rolesTXT = rolesTXT + "---------------------------------------------------------------\n"
rolesTXT = rolesTXT + "Morgana \U000027a1 É espiã. Ela pode tentar enganar o Percy e fingir ser o Merlin e ganhar alguma vantagem no jogo\n"
rolesTXT = rolesTXT + "\nDesbloqueada por: Percy\nDesbloqueia: Ninguém\n"
rolesTXT = rolesTXT + "---------------------------------------------------------------\n"
################## flip message ########################################################
def receiveMessage():
	global old_id
	x = len(Queue)
	while x > 0:
		avalon.quit(Queue[x-1])
		Queue.pop()
		x = x - 1

	while 1:
		time.sleep(0.1)
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

	def myTeam(self,cand,total):
		ans = []
		l = len(cand)
		while total > 0:
			pi = random.randint(0,l-1)
			ans.append(cand[pi])
			cand.pop(pi)
			l = l -1
			total = total - 1
		return ans

	def approveMission(self):
		x = random.randint(0,2)
		if x == 0:
			return False
		else:
			return True

	def sabotage(self):
		if self.spy == False:
			return False
		x = random.randint(0,1)
		if x == 0:
			return True
		else:
			return False

	def whoIsMerlin(self,L):
		valor = random.randint(0,len(L) - 1)
		return L[valor]

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
		self.Spoints = 0
		self.Rpoints = 0
		self.curr = 0
		self.consecutive = 3
		self.action = ""
		self.currTeam = []
		self.candidates = []
		self.remain = -1
		self.privateMessage = []
		self.approve = 0
		self.denied = 0
		self.waitingVote = []
		self.currVote = ""
		self.fails = 0
		self.comandRemain = 0

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
		if data not in self.messageSetting.roles:
			return None
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
		x = "ok"
		return x

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
		totalSpy = self.spies - totalSpy 
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
			sendMessage(P.id,str(emoji)+"\n\nVocê é o MERLIN\n\n"+
				"Os espiões são:\n\n" + str(retorno)+"\n\n" + str(emoji),temp = 0.1)

		elif "Morgana" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			sendMessage(P.id,str(emoji)+"\n\nVocê é a MORGANA\n\n"+
				"Os outros espiões são:\n\n"+str(retorno)+"\n\n"+str(emoji),temp = 0.1)

		elif "Percy" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if ("Merlin" in x.roles) or ("Morgana" in x.roles):
					retorno = retorno + " - " + x.name
			sendMessage(P.id,str(emoji)+"\n\nVocê é o PERCY\n\n"+
				"O Merlin é um desses jogadores:\n\n" + str(retorno)+"\n\n"+str(emoji),temp = 0.1)

		elif "Assassin" in P.roles:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			sendMessage(P.id,str(emoji)+"\n\nVocê é o ASSASSINO\n\n"+
				"Os outros espiões são:\n\n"+ str(retorno)+"\n\n"+str(emoji),temp = 0.1)

		elif P.spy:
			retorno = ""
			for x in self.players:
				if x.name == P.name:
					continue
				if x.spy or ("Palm" in x.roles):
					retorno = retorno + " - " + x.name
			sendMessage(P.id,str(emoji)+"\n\nVocê é um ESPIÃO\n\n"+
				"Os outros espiões são:\n\n" + str(retorno)+"\n\n"+str(emoji),temp = 0.1)
		else:
			sendMessage(P.id,str(emoji)+"\n\nVocê é da RESISTÊNCIA\n\n" + 
				"Ajude seu time a vencer!\n\n"+str(emoji),temp = 0.1)

	def sendAllInfo(self):
		for P in self.players:
			self.sendInfo(P)

	def printAllInfo(self):
		self.comandRemain = 0
		for P in self.players:
			if P.isBot == False:
				self.comandRemain = self.comandRemain + 1
				Fila.append((P.name,self.id))
			print(P.name,': ',P.roles)

	def setVariables(self):
		if self.totalPlayers == 5 or self.totalPlayers == 6:
			self.spies = 2
		elif self.totalPlayers>= 7 or self.totalPlayers <= 9:
			self.spies = 3
		else:
			self.spies = 4

		self.history = "\U000023EA    Histórico    \U000023EA\n\n"
		self.history = self.history + "Missão 1:\n\n"
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
		sendMessage(to,text,temp = 0.1)

	def getHistory(self,to):
		
		sendMessage(to,self.history,temp = 0.1)

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
		sendMessage(to,text,temp = 0.1)

	def editVoteMessage(self):
		
		text = "Aguardando os votos de: ["
		for x in self.waitingVote:
			text = text + " " + x
		text = text + "]"
		bot.editMessageText(msg_identifier = (self.id,self.privateMessage[0]),text = text,
			reply_markup = InlineKeyboardMarkup(
				inline_keyboard = [
				[InlineKeyboardButton(text = "Aprovar",callback_data = "accept"),
				InlineKeyboardButton(text = "Recusar",callback_data = "denied")]]))
		time.sleep(1)

	def endOfGame(self,text):
		
		for x in self.players:
			if x.spy:
				text = text + "\U0001F534"
			else:
				text = text + "\U0001F535"
			text = text + x.name + ": "
			for y in x.roles:
				text = text + y + " "
			text = text + "\n"
		sendMessage(self.id,text)
		Queue.append(self.id)

	def pointForSpies(self,text):
		
		self.Spoints = self.Spoints + 1
		if self.Spoints == 3:
			text = text + "\U0001F534   Vitória dos ESPIÕES   \U0001F534\n\n\n"
			self.endOfGame(text)
		else:
			
			sendMessage(self.id,text + "Ponto para os espiões\nEspiões: " + str(self.Spoints)+
				"\nResistência: " + str(self.Rpoints))
			self.consecutive = 3
			self.state = self.state + 1
			self.curr = self.curr + 1
			if self.curr >= self.totalPlayers:
				self.curr = 0
			self.history = self.history + "\nMissão " + str(self.state) + ":\n\n"
			self.chooseTheTeam()

	def checkMerlin(self,think):

		ans = ""
		for x in range(self.totalPlayers):
			if "Merlin" in self.players[x].roles:
				ans = self.players[x].name
				break
		if ans == think:
			sendMessage(self.id,text = "O assassino matou "+think+
				". " + think + " era o Merlin")
			texto = "\U0001F534   Vitória dos ESPIÕES   \U0001F534\n\n\n"
		else:
			sendMessage(self.id,text = "O assassino matou "+think+
				". " + think + " não era o Merlin")
			texto = "\U0001F535   Vitória da RESISTÊNCIA   \U0001F535\n\n\n"
		self.endOfGame(texto)

	def killMerlin(self):
		x = 0
		L = []
		botzin = False
		lista = []
		rob = None
		while x < self.totalPlayers:
			if "Assassin" in self.players[x].roles:
				if self.players[x].isBot:
					botzin = True
					rob = self.players[x]
				else:
					Mid = self.players[x].id
			else:
				lista.append(self.players[x].name)
				L.append([InlineKeyboardButton(text = self.players[x].name,
					callback_data = str(self.id) + "$" + str(self.players[x].name))])
			x = x + 1
		bot.sendMessage(self.id,"\U000026D4   O assassino está tentando matar o Merlin...")
		if botzin:
			data = rob.whoIsMerlin(lista)
			self.checkMerlin(data)
		else:
			r = bot.sendMessage(Mid,text = "Você é o assassino. Mate o Merlin!",reply_markup = InlineKeyboardMarkup(
				inline_keyboard = L))
			self.privateMessage.append(r['message_id'])
			self.action = "Merlin"

	def pointForResistance(self,text):
		
		self.Rpoints = self.Rpoints + 1
		sendMessage(self.id,text + "Ponto para a resistência\nEspiões: " + str(self.Spoints)+
				"\nResistência: " + str(self.Rpoints))
		if self.Rpoints == 3:
			if "Merlin" in self.roles:
				self.killMerlin()
			else:
				text = text + "\U0001F535   Vitória da RESISTÊNCIA   \U0001F535\n\n\n"
				self.endOfGame(text)
		else:		
			self.consecutive = 3
			self.state = self.state + 1
			self.curr = self.curr + 1
			if self.curr >= self.totalPlayers:
				self.curr = 0
			self.history = self.history + "\nMissão " + str(self.state) + ":\n\n"
			self.chooseTheTeam()

	def showResultMission(self):
		if self.fails >= self.needToFail[self.state - 1]:
			text = "\U0001F534    A missão foi SABOTADA    \U0001F534\n\n"
			text = text + "Votos para falhar: " + str(self.fails) + "\n"
			text = text + "----------------------------------------------\n\n"
			self.history = self.history + text
			self.pointForSpies(text)
		else:
			text = "\U0001F535    A missão foi um SUCESSO    \U0001F535\n\n"
			text = text + "Votos para falhar: " + str(self.fails) + "\n"
			text = text + "----------------------------------------------\n\n"
			self.history = self.history + text
			self.pointForResistance(text)

	def gotoMission(self):
		
		self.action = "Mission"
		self.fails = 0
		text = "\U00002709 O time foi enviado à missão...\n\nAguardando o resultado."
		sendMessage(self.id,text)
		x = 0
		while x < self.totalPlayers:
			if self.players[x].name not in self.currTeam:
				x = x + 1
				continue
			if self.players[x].isBot:
				if self.players[x].spy:
					if self.players[x].sabotage():
						self.fails = self.fails + 1
			elif self.players[x].spy:
				r = bot.sendMessage(self.players[x].id,text="O que você deseja fazer nesta missão?",
					reply_markup = InlineKeyboardMarkup(
						inline_keyboard = [
							[InlineKeyboardButton(text = "Passar",callback_data = str(self.id) + "$pass"),
							InlineKeyboardButton(text = "Sabotar",callback_data = str(self.id) + "$fail")]
						]))
				self.privateMessage.append(r['message_id'])
			else:
				r = bot.sendMessage(self.players[x].id,text = "O que você deseja fazer nesta missão?",
					reply_markup = InlineKeyboardMarkup(
						inline_keyboard = [
							[InlineKeyboardButton(text = "Passar",callback_data = str(self.id) + "$pass")]
						]))
				self.privateMessage.append(r['message_id'])
			self.currTeam.remove(self.players[x].name)
			x = x + 1
		if len(self.privateMessage) == 0:
			self.showResultMission()

	def showResultTeam(self):
		
		bot.deleteMessage(msg_identifier = (self.id,self.privateMessage[0]))
		self.privateMessage.pop()
		if self.approve > self.denied:
			self.currVote = self.currVote + "\nTime aprovado\n"
		else:
			self.currVote = self.currVote + "\nTime negado\n----------------------------------------\n"
		sendMessage(self.id,self.currVote)
		self.history = self.history + self.currVote
		self.currVote = ""

		if self.approve > self.denied:
			self.gotoMission()
		elif self.consecutive == 0:
			self.curr = self.curr + 1
			if self.curr >= self.totalPlayers:
				self.curr = 0
			text = "\U0001F6A8 Limite de rejeições atingido \U0001F6A8\n\n"
			self.pointForSpies(text)
		else:
			self.curr = self.curr + 1
			self.consecutive = self.consecutive - 1
			if self.curr >= self.totalPlayers:
				self.curr = 0
			self.chooseTheTeam()

	def voteReceived(self,who,vote):
		if who not in self.waitingVote:
			return None
		self.waitingVote.remove(who)
		if vote == "accept":
			self.approve = self.approve + 1
			self.currVote = self.currVote + who + "\U00002705\n"
		else:
			self.denied = self.denied + 1
			self.currVote = self.currVote + who + "\U0000274C\n"
		if len(self.waitingVote) == 0:
			self.showResultTeam()
		else:
			self.editVoteMessage()

	def isTeamOk(self):
		
		text = ""
		if self.players[self.curr].isBot:
			text = text + str(self.players[self.curr].name)
		else:
			text = text + "@" + str(self.players[self.curr].name)
		text = text + " escolheu:\n\n"
		for x in self.currTeam:
			text = text + "- " + str(x) + "\n"
		text = text + "\n" + "Você aprova o time?"
		sendMessage(self.id,text)
		self.action = "voteTeam"
		self.approve = 0
		self.denied = 0
		self.currVote = "\nO líder " + str(self.players[self.curr].name) + " formou o time:\n["
		for x in self.currTeam:
			self.currVote = self.currVote + " " + x
		self.currVote = self.currVote + "]\n\nResultado dos votos para aprovação do time:\n"

		for x in self.players:
			if x.isBot:
				ans = x.approveMission()
				if ans:
					self.approve = self.approve + 1
					self.currVote = self.currVote + x.name + "\U00002705\n"
				else:
					self.denied = self.denied + 1
					self.currVote = self.currVote + x.name + "\U0000274C\n"
			else:
				self.waitingVote.append(x.name)
		tam = len(self.privateMessage) #usar o mesmo pois porém, né
		while tam > 0:
			self.privateMessage.pop()
			tam = tam-1
		r = sendMessage(self.id,text = "votação abrirá em segundos...")
		self.privateMessage.append(r['message_id'])
		self.editVoteMessage()

	def msgLeader(self):
		
		text = "Você é o líder da missão. Escolha mais " + str(self.remain) + " jogadores para formar o time\n"
		text = text + "Time atual:\n"
		L = []
		for x in self.currTeam:
			text = text + "- " + str(x) + "\n"
		for x in self.candidates:
			R = []
			data = str(self.id) + "$" + str(x)
			R.append(InlineKeyboardButton(text = str(x),callback_data = data))
			L.append(R)
		r = sendMessage(self.players[self.curr].id,text = text,
			reply_markup = InlineKeyboardMarkup(inline_keyboard = L))
		self.privateMessage.append(r['message_id'])

	def editMsgLeader(self):
		
		text = "Você é o líder da missão. Escolha mais " + str(self.remain) + " jogadores para formar o time\n"
		text = text + "Time atual:\n"
		L = []
		for x in self.currTeam:
			text = text + "- " + str(x) + "\n"
		for x in self.candidates:
			R = []
			data = str(self.id) + "$" + str(x)
			R.append(InlineKeyboardButton(text = str(x),callback_data = data))
			L.append(R)
		if self.remain == 0:
			L = None
		bot.editMessageText(msg_identifier = (self.players[self.curr].id,self.privateMessage[0]),
							text = text,reply_markup = InlineKeyboardMarkup(
								inline_keyboard = L))
		time.sleep(1)

	def chooseTheTeam(self):
		
		text = "\U00002709    Missão " + str(self.state) + "    \U00002709\n\n"
		text = text + "\U00002B50 "
		if self.players[self.curr].isBot:
			text = text + str(self.players[self.curr].name)
		else:
			text = text + "@" + str(self.players[self.curr].name)
		text = text + ", Você é o líder da missão. Escolha " + str(self.mission[self.state-1])
		text = text + " jogadores para formar seu time. Lembre-se, "
		if self.needToFail[self.state - 1] == 1:
			text = text + "é necessária apenas uma falha para a missão ser sabotada, caso o time seja aprovado"
		else:
			text = text + "são necessárias " + str(self.needToFail(self.state-1)) + " falhas para a missão ser sabotada,"
			text = text + " caso o time seja aprovado"
		
		sendMessage(self.id,text)
		self.remain = self.mission[self.state-1]
		self.currTeam = []
		self.candidates = getNames(self.players)

		if self.players[self.curr].isBot:
			self.currTeam = self.players[self.curr].myTeam(cand = self.candidates,total = self.mission[self.state-1])
			self.remain = 0
			self.candidates = []
			self.isTeamOk()
		else:
			self.action = "choose"
			self.msgLeader()

	def failMission(self,data,mid,cid):
		if data == "pass":
			bot.editMessageText(msg_identifier = (cid,mid),text = "Você decidiu passar a missão.",reply_markup = None)
		else:
			self.fails = self.fails + 1
			bot.editMessageText(msg_identifier = (cid,mid),text = "Você decidiu sabotar a missão.",reply_markup = None)
		if len(self.privateMessage) == 0:
			self.showResultMission()

	def updateTeam(self,p):
		if p not in self.candidates:
			return None
		self.remain = self.remain - 1
		self.candidates.remove(p)
		self.currTeam.append(p)
		self.editMsgLeader()
		if self.remain == 0:
			self.privateMessage.pop()
			self.isTeamOk()

	def initGame(self):
		
		self.state = 1
		self.setVariables()
		self.shuffle()
		if "Palm" in self.roles:
			self.players[0].roles.append("Palm")
		self.shuffle()
		self.setRoles()
		self.shuffle()
		self.printAllInfo()
		sendMessage(self.id,"\U0001F534\U0001F535 Por favor, cliquem no botão abaixo e enviem o comando /view para"+
			" visualizar seu papel no jogo. \U0001F534\U0001F535\n\nAguardando os comandos...",reply_markup = InlineKeyboardMarkup(
				inline_keyboard = [[InlineKeyboardButton(text = "Envie-me o comando",url = "t.me/avalon_kinhobot")]]))
		self.shuffle()

	def initGame2(self):
		self.sendAllInfo()
		self.remember(self.id)
		self.chooseTheTeam()


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
	def findGame(self,idG):
		pos = 0
		while pos < self.currentGames:
			print(self.games[pos].id,' + ',idG)
			if str(self.games[pos].id) == str(idG):
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
####################### getNames ######################################################
def getNames(L):
	LL = []
	for x in L:
		LL.append(x.name)
	return LL
####################### remove #########################################################
def remove(txt):
	sz = len(Fila)
	idx = []
	for i in range(sz):
		if txt == Fila[i][0]:
			idx.append(Fila[i])
			x = avalon.findGame(Fila[i][1])
			avalon.games[x].comandRemain = avalon.games[x].comandRemain - 1
			if avalon.games[x].comandRemain == 0:
				avalon.games[x].initGame2()
	sz = len(idx)
	for i in range(sz):
		Fila.remove(idx[i])

###################### send Message ####################################################
def sendMessage(to,text,reply_markup = None,temp = 3):
	print('id -> ',to) #id user = 686267431
  while 1:
    try:
      r = bot.sendMessage(to,text = text,reply_markup = reply_markup)
      break
    except:
      time.sleep(temp)
	return r

####### some global variables ##########################################################
sentMessage = None
avalon = general()
Queue = []
Fila = []

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
	if '/roles' == msg['message']['text']:
		bot.sendMessage(msg['message']['from']['id'],rolesTXT)
	if '/view' == msg['message']['text']:
		remove(msg['message']['from']['username'])

############################## group mode #############################################
def groupMode(msg):
	global avalon

	if '/newgame' in msg['message']['text']:
		if isRunning(msg['message']['chat']['id']) != -1:
			sendMessage(msg['message']['chat']['id'],'Um jogo já foi iniciado. Digite /join para entrar ou /quitgame para finalizar o jogo atual')
		else:
			avalon.newgame(msg['message']['chat']['id'])
			avalon.join(msg['message']['from']['id'],msg['message']['from']['username'],msg['message']['chat']['id'])
			sendMessage(msg['message']['chat']['id'],"Novo jogo criado\U00002705\n\nDigite /join para entrar\n\n"
					+"Digite /leave para sair\n\nDigite /quitgame para finalizar este jogo\n\n"+
					"Digite /startgame para a diversão começar\n\n"+"Estou ativo em "+
					str(avalon.currentGames)+" grupos no momento")
			retMsg = sendMessage(msg['message']['chat']['id'],
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
		return None #break
	if '/quitgame' in msg['message']['text']:
		avalon.quit(msg['message']['chat']['id'])
		sendMessage(msg['message']['chat']['id'],"Jogo finalizado.")
		return None

	x = avalon.findGame(msg['message']['chat']['id']) ## find the game

	if '/startgame' in msg['message']['text']:
		if avalon.games[x].owner != msg['message']['from']['username']:
			sendMessage(msg['message']['chat']['id'],"Só @" + avalon.games[x].owner + " pode iniciar"+
				", pois ele criou a partida.")
			return None
		if avalon.games[x].state != 0:
			sendMessage(msg['message']['chat']['id'],"Você já iniciou este jogo. Digite /quitgame para finalizar"+
				" o jogo atual")
			return None
		if avalon.games[x].totalPlayers < 5:
			sendMessage(msg['message']['chat']['id'],'Quantidade mínima de jogadores não atingida\U0001F625'+
				"\nIrei completar com alguns bots\U0001F47E")
			avalon.games[x].addBots(5 - avalon.games[x].totalPlayers)
			avalon.games[x].initGame()
		else:
			avalon.games[x].initGame()
		return None

	if '/join' in msg['message']['text']:
		if avalon.games[x].state != 0:
			sendMessage(msg['message']['chat']['id'],"Você não pode realizar esta operação, o jogo já foi iniciado.")
			return None
		flag = avalon.join(msg['message']['from']['id'],msg['message']['from']['username'],msg['message']['chat']['id'])
		if flag:
			sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' se juntou ao game \U0000270C')
		else:
			sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' não se preocupe, você já estava no jogo \U00002714')
		return None
	if '/leave' in msg['message']['text']:
		if avalon.games[x].state != 0:
			sendMessage(msg['message']['chat']['id'],"Você não pode realizar esta operação, o jogo já foi iniciado.")
			return None
		flag = avalon.leave(msg['message']['from']['id'],msg['message']['chat']['id'])
		if flag:
			sendMessage(msg['message']['chat']['id'],
				'@'+msg['message']['from']['username'] + ' ficou com medo e saiu do jogo \U0001F61D')
			if avalon.games[x].totalPlayers == 0:
				avalon.quit(msg['message']['chat']['id'])
				sendMessage(msg['message']['chat']['id'],"Por que todo mundo saiu? Jogo finalizado")
				sendMessage(msg['message']['chat']['id'],"\U0001F63F")
				return None
			if msg['message']['from']['username'] == avalon.games[x].owner:
				avalon.games[x].owner = avalon.games[x].players[0].name
				bot.editMessageText(msg_identifier = avalon.games[x].getSettingIdentifier(),
						text = avalon.games[x].getSettingText(),
						reply_markup = avalon.games[x].getSettingReply())
				time.sleep(1)
		else:
			sendMessage(msg['message']['chat']['id'],
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
		if 'private' == msg['callback_query']['message']['chat']['type']:
			data = str(msg['callback_query']['data']).split("$")
			x = avalon.findGame(str(data[0]))
			if x == -1:
				continue
			if avalon.games[x].state == 0:
				continue
			if msg['callback_query']['message']['message_id'] in avalon.games[x].privateMessage:
				if avalon.games[x].action == "choose":
					avalon.games[x].updateTeam(str(data[1]))
				elif avalon.games[x].action == "Mission":
					avalon.games[x].privateMessage.remove(msg['callback_query']['message']['message_id'])
					avalon.games[x].failMission(data = data[1],mid = msg['callback_query']['message']['message_id'],
						cid = msg['callback_query']['message']['chat']['id'])
				elif avalon.games[x].action == "Merlin":
					bot.editMessageText(msg_identifier = (msg['callback_query']['message']['chat']['id'],
						msg['callback_query']['message']['message_id']),text= "Você escolheu matar " + str(data[1]),reply_markup = None)
					avalon.games[x].privateMessage.remove(msg['callback_query']['message']['message_id'])
					avalon.games[x].checkMerlin(data[1])
		else:
			x = avalon.findGame(msg['callback_query']['message']['chat']['id'])
			if x != -1:
				if avalon.games[x].state == 0 and msg['callback_query']['message']['message_id'] == avalon.games[x].messageSetting.msgId:
					if msg['callback_query']['from']['username'] == avalon.games[x].owner:
						r = avalon.games[x].settingUpdate(msg['callback_query']['data'])
						if r == None:
							continue
						bot.editMessageText(msg_identifier = avalon.games[x].getSettingIdentifier(),
							text = avalon.games[x].getSettingText(),
							reply_markup = avalon.games[x].getSettingReply())
						time.sleep(1)
				elif avalon.games[x].state != 0 and avalon.games[x].action == "voteTeam":
					if msg['callback_query']['from']['username'] in avalon.games[x].waitingVote:
						avalon.games[x].voteReceived(msg['callback_query']['from']['username'],msg['callback_query']['data'])
