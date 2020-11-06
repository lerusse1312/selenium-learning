from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
#import selenium wait for load 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "/usr/bin/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)

#Open the page
driver.get("http://www.google.com")

#Get searchbar
search = driver.find_element_by_name("q")

search.send_keys("quebecsocialist")
search.submit()

#Wait for page to load
try:
    #click my twitter link
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "QuebecSocialist"))
    ).click()
finally:
    time.sleep(10)
    driver.quit()