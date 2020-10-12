import hashlib
import hmac
import base64
import random
import sys
import math

def provabilitySeed(dailySecret,clientSecret,nonce):

	clientSecretAndNounce = clientSecret+"-"+str(nonce)

	hmacOutput = hmac.new(dailySecret.encode('utf8'), clientSecretAndNounce.encode('utf8'), hashlib.sha512).hexdigest()
	return(hmacOutput)
	
def rpsSelectionBot(clientSeed,nonce,serverSeed):
	
	alternatives = ["rock","paper","scissors"]
	
	combinedSeed = provabilitySeed(serverSeed,clientSeed,nonce)

	random.seed(combinedSeed)
	random.shuffle(alternatives)
	result = {"result":alternatives[0],"nonce":nonce,"clientSeed":clientSeed}
	
	return result

def flipCoin(clientSeed,nonce,serverSeed):
	
	coinSides = ["Heads","Tails"]
	
	combinedSeed = provabilitySeed(serverSeed,clientSeed,nonce)
	
	random.seed(combinedSeed)
	random.shuffle(coinSides)
	result = {"result":coinSides[0],"nonce":nonce,"clientSeed":clientSeed}
	
	return result
	
def playBank(clientSeed,nonce,serverSeed):
	
	bankList = ["Lose","Lose"] + (["Win"] * 100)
	
	combinedSeed = provabilitySeed(serverSeed,clientSeed,nonce)

	random.seed(combinedSeed)
	random.shuffle(bankList)
	result = {"result":bankList[0],"nonce":nonce,"clientSeed":clientSeed}
	
	return result

def playDice(clientSeed,nonce,serverSeed,diceMax):
	
	diceSides = list(range(1, (diceMax+1)))
	
	combinedSeed = provabilitySeed(serverSeed,clientSeed,nonce)

	random.seed(combinedSeed)
	random.shuffle(diceSides)
	result = {"result":diceSides[0],"nonce":nonce,"clientSeed":clientSeed}
	
	return result

counterHeads = 0
counterTails = 0

def playCrash(clientSeed,nonce,serverSeed):
	
	combinedSeed = provabilitySeed(serverSeed,clientSeed,nonce)

	random.seed(combinedSeed)
	
	i = random.random()
	i = 0.99/(1-i)

	i = max(i,1.0)
	i = math.floor(i*100)/100
	
	result = {"result":i,"nonce":nonce,"clientSeed":clientSeed}
	return result

if sys.argv[1] == "bank":
	for i in range(int(sys.argv[3]), int(sys.argv[4])):
		print(playBank(sys.argv[2],i,sys.argv[5]))
elif sys.argv[1] == "flip":
	for i in range(int(sys.argv[3]), int(sys.argv[4])):
		result = flipCoin(sys.argv[2],i,sys.argv[5])
		print(result)
		if result['result'] == "Heads":
			counterHeads = counterHeads +1
		else:
			counterTails = counterTails +1
	print(str(counterHeads),str(counterTails))
elif sys.argv[1] == "rps":
	for i in range(int(sys.argv[3]), int(sys.argv[4])):
		print(rpsSelectionBot(sys.argv[2],i,sys.argv[5]))
elif sys.argv[1] == "dice":
	for i in range(int(sys.argv[3]), int(sys.argv[4])):
		result = playDice(sys.argv[2],i,sys.argv[5],int(sys.argv[6]))
		print(playDice(sys.argv[2],i,sys.argv[5],int(sys.argv[6])))
elif sys.argv[1] == "crash":
	for i in range(int(sys.argv[3]), int(sys.argv[4])):
		result = playCrash(sys.argv[2],i,sys.argv[5])
		print(result)

else:
	print("Invalid game")
