import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

#Credentials
base_url = "http://www.omegle.com"


#Init needed
driver = webdriver.Firefox()

#Total chat log
logs = None
chatIndex = 1 

# Always init to 1 because of "Youre now chatting with random stranger"
logSize = 1 
ticks = 0 

chatLog = []
staticResponses = ["ASL?", "Whats gucci", "How are you my friend", "I am artistic", "Introduce me to your maplestory grand wizards"]

def doesExist(name, classification):
	try:
		if (classification == "class"):
			driver.find_element_by_class_name(name)
	except NoSuchElementException:
			return False
	return True

def wait_id(seconds, id):
	try:
		ele = WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.ID, id)))
	finally:
		print "Could not find ID"
		driver.quit()

def wait_implicitly(seconds):
	driver.implicitly_wait(seconds)

def wait_sleep(seconds):
	time.sleep(seconds)

ignoreList = ["Stranger is typing..."]

def sendMessage(message):
	chatBox = driver.find_element_by_class_name("chatmsg")
	chatBox.send_keys(message, Keys.RETURN)
def getChat():
	global logs
	global chatIndex
	global logSize
	global chatLog
	global ticks
	logs = driver.find_elements_by_class_name("logitem")
	if (len(logs)-1 == logSize):
		if logs[chatIndex].text not in ignoreList:
			logSize = len(logs)
			print logs[chatIndex].text	
			#print "ChatIndex:", chatIndex
			#print "Log len:", logSize 
			#chatLog.append(logs[chatIndex].text)
		
			#Type if it's your turn.
			if "Stranger" in logs[chatIndex].text:
				wait_sleep(1)
				sendMessage(random.choice(staticResponses))
			chatIndex += 1
			


	#Conversation ends			
	elif (len(logs)-1 > logSize):
		print "Chat has ended!"
		#Start new conversation
		try:
			newConvo = driver.find_element_by_class_name("disconnectbtn")
			newConvo.click()
			ticks = 0
			chatIndex = 1
			logSize = 1
		except:
			print "Cannot click nonexistant shit"
	#Counts ticks to prevent getting stuck	
	else:
		ticks += 1
		if ticks > 10:
			newConvo = driver.find_element_by_class_name("disconnectbtn")
			try:
				newConvo.click()
				newConvo.click()		
			except:
				print "Cannot click nonexistant shit"
			ticks = 0
			chatIndex = 1
			logSize = 1	
	
def init():
	driver.get(base_url)
	textButton = driver.find_element_by_id("textbtn")
	textButton.click()
	wait_sleep(1)
	
	sendMessage(random.choice(staticResponses))	
	while True:
		wait_sleep(1)
		getChat()
			

def main():
	init()	


main()

