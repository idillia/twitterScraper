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

import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def findTwitterHandler(ppl):	

	profileName = ppl.text
	profile = ppl.get_attribute("href")
	print(profileName)

	main_window = driver.current_window_handle

	# print "Profile name: %s," % (profileName)
	# print "Open window: %s," % (main_window)
	
	script = '''window.open("%s", "Whatever")''' % (profile)

	driver.execute_script(script)
	next_window = driver.window_handles[1]
	driver.switch_to_window(next_window)
	

	# print "All windows: %s," % (driver.window_handles)
	# print "Swtched to window: %s," % (next_window)
	# print "Current window: %s," % driver.current_window_handle

	driver.execute_script(script)
	time.sleep(10)
	try: 
		location =  driver.find_element_by_css_selector('span.tag > span.fontello-location:first-of-type + a').text
		# print(location)
		position = driver.find_element_by_css_selector('span.tag > span.fontello-tag-1:first-of-type +a').text
		# print(position)	
		linkedin = driver.find_element_by_css_selector("*[class^='icon link_el fontello-linkedin']").get_attribute("href")
		# print(linkedin)
		

		handler = driver.find_element_by_css_selector("*[class^='icon link_el fontello-twitter']")
		twitterLink = handler.get_attribute("href")	
		# print(twitterLink)
		
		
		with open("handlersData.csv", "a") as scrapedDataFile:
			scrapedDataFileWriter = csv.writer(scrapedDataFile)
			scrapedDataFileWriter.writerow([profileName, twitterLink, location, position, linkedin])

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

# listOfPeople = 

persons = []

# for person in driver.find_elements_by_css_selector('a[class="u-colorGray3 u-uncoloredLink"][data-type="User"]'):
# 	# print(person.get_attribute("href"))
# 	findTwitterHandler(person)	

for x in range(96,180):
	u = driver.find_elements_by_css_selector('a[class="u-colorGray3 u-uncoloredLink"][data-type="User"]')[x]
	findTwitterHandler(u)





