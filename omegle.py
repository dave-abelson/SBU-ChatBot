from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

#Credentials
base_url = "http://www.omegle.com"


#Init needed
driver = webdriver.Firefox()


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

	

def init():
	driver.get(base_url)
	textButton = driver.find_element_by_id("textbtn")
	textButton.click()
	wait_implicitly(3)
	chatBox = driver.find_element_by_class_name("chatmsg")
	chatBox.send_keys("I love pussy", Keys.RETURN)	

def main():
	init()	


main()

