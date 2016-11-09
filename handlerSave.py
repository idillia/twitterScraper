import config
from config import _user, _pw
import csv
import selenium
from selenium import webdriver
chrome_path = r"/Users/mila/Downloads/chromedriver"
driver = webdriver.Chrome(chrome_path)

driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")	
driver.implicitly_wait(20)
driver.find_element_by_id("email").send_keys(_user)
driver.find_element_by_name("pass").send_keys(_pw)
driver.implicitly_wait(30)
driver.find_element_by_id("loginbutton").click()

driver.implicitly_wait(120)

driver.get("https://www.quora.com/profile/Pei-Patrick-Kuo")
driver.implicitly_wait(20)
driver.find_element_by_css_selector("*[class^='header_signin_with_search_bar action_button']").click()


handler = driver.find_element_by_xpath("""//*/div/div[4]/a""")

twitterLink = handler.get_attribute("href")
print(twitterLink)

# driver.quit()
with open("handlersData.csv", "r") as scrapedDataFile:
	scrapedDataFileReader = csv.reader(scrapedDataFile)
	scrapedList = []
	for row in scrapedDataFileReader:
		if len (row) != 0:
			scrapedList = scrapedList + [row]		

scrapedDataFile.close()

print(scrapedList)	

with open("handlersData.csv", "a") as scrapedDataFile:
	scrapedDataFileWriter = csv.writer(scrapedDataFile)
	scrapedDataFileWriter.writerow(['/n', twitterLink])

scrapedDataFile.close()
