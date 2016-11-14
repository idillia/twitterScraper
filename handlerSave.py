import config
from config import _user, _pw
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

# driver.get("https://www.quora.com/profile/Pei-Patrick-Kuo")
driver.get("https://www.quora.com/topic/Company-Culture/writers")
driver.implicitly_wait(20)

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
# elm = driver.find_element_by_tag_name('html')
# elm.send_keys(Keys.END)
# time.sleep(8)
# driver.find_element_by_css_selector("*[class^='header_signin_with_search_bar']").click()
# driver.implicitly_wait(20)
# list = driver.find_elements_by_css_selector("*[class='user']")

list = driver.find_element_by_css_selector("a[href*='profile']")
print(list)
print(list.text)
# listId = driver.find_elements_by_id("_name_link")
listId1 = driver.find_elements_by_xpath('//div[13]/a')


# print(list)
# driver.implicitly_wait(40)

# for el in list:
# 	# if len (el.text) !=0:
# 	driver.implicitly_wait(5)
# 	print(el)
# 	print(el.text)
# 	print(el.get_attribute("href"))
		# el.click()

		# el.click()
		
# print(list[4])
# list[4].click()

# driver.quit()
# list[1].click()

# handler = driver.find_element_by_xpath("""//*/div/div[4]/a""")

# twitterLink = handler.get_attribute("href")
# print(twitterLink)



# .get_attribute("href")


# driver.quit()	
# with open("handlersData.csv", "r") as scrapedDataFile:
# 	scrapedDataFileReader = csv.reader(scrapedDataFile)
# 	scrapedList = []
# 	for row in scrapedDataFileReader:
# 		if len (row) != 0:
# 			scrapedList = scrapedList + [row]		

# scrapedDataFile.close()


# print(scrapedList)	

# with open("handlersData.csv", "a") as scrapedDataFile:
# 	scrapedDataFileWriter = csv.writer(scrapedDataFile)
# 	scrapedDataFileWriter.writerow(['/n', twitterLink])

# scrapedDataFile.close()


# Actions action = new Actions(webdriver);
# WebElement we = webdriver.findElement(By.xpath("html/body/div[13]/ul/li[4]/a"));
# action.moveToElement(we).moveToElement(webdriver.findElement(By.xpath("/expression-here"))).click().build().perform();
