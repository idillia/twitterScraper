# -*- coding: utf-8 -*-
# import data
# from data import _prof
import csv
import selenium
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def findTwitterHandler(path):	
			
	profileName = driver.find_element_by_xpath(path).text
	profile = driver.find_element_by_xpath(path).get_attribute("href")

	main_window = driver.current_window_handle

	print "Profile XpathString: %s," % (profileXpathString)     
	print "Profile name: %s," % (profileName)
	print "Open window: %s," % (main_window)
	
	script = '''window.open("%s", "Whatever")''' % (profile)

	driver.execute_script(script)
	next_window = driver.window_handles[1]
	driver.switch_to_window(next_window)
	

	print "All windows: %s," % (driver.window_handles)
	print "Swtched to window: %s," % (next_window)
	print "Current window: %s," % driver.current_window_handle

	driver.execute_script(script)
	try: 
		handler = driver.find_element_by_css_selector("*[class^='icon link_el fontello-twitter']")
		twitterLink = handler.get_attribute("href")
		print(twitterLink)
		
		with open("handlersData.csv", "a") as scrapedDataFile:
			scrapedDataFileWriter = csv.writer(scrapedDataFile)
			scrapedDataFileWriter.writerow([profileName, twitterLink])

		scrapedDataFile.close()
		print "Profile saved"
		driver.close()
	except NoSuchElementException: 
		driver.close()   

	driver.switch_to_window(main_window)
	sleep(2) #wait until new tab finishes loading
	return;



chrome_path = r"/Users/mila/Downloads/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(120)

driver.set_page_load_timeout(30)
driver.get("https://angel.co/people/all")	
driver.implicitly_wait(20)
time.sleep(60)

# moreBtn = driver.find_element_by_css_selector("*[class^='more_link u-unstyledLink u-textShadowWhite']").click()
# print "Button is clicked %s " % (moreBtn)




listOfPeople = driver.find_elements_by_css_selector("a[href*='?utm_source=people']")

print(listOfPeople)


# for x in range(1,):
# 	if x <= 12:
# 		profileXpathString = '''//*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[%s]/div/div[1]/div/div[2]/div[1]/a''' % (x)
# 		print "Loop counter:  %d" % (x)
# 		findTwitterHandler(profileXpathString)
		
# 	elif x > 12 and x <= 24:
# 		for y in range(1, 13):
# 			profileXpathString = '''//*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[%s]/div/div[1]/div/div[2]/div[1]/a''' % (y)
# 			print(profileXpathString)
# 			findTwitterHandler(profileXpathString)
# 	elif x > 24 and x <= 36:
# 		for c in range(1, 13):
# 			profileXpathString = '''//*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[13]/div[%s]/div/div[1]/div/div[2]/div[1]/a''' % (c)
# 			print(profileXpathString)
# 			findTwitterHandler(profileXpathString)

	
# //*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[12]/div/div[1]/div/div[2]/div[1]/a

# //*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[12]/div/div[1]/div/div[2]/div[1]/a

# //*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[13]        /div[12]/div/div[1]/div/div[2]/div[1]/a

# //*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[13]/div[13]/div[11]/div/div[1]/div/div[2]/div[1]/a
# //*[@id="root"]/div[4]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[13]/div[13]/div[13]/div[12]/div/div[1]/div/div[2]/div[1]/a




