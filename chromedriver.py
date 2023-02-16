from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
sample codes for using Chromedriver
'''

service = Service('/usr/bin/chromedriver')  # url for the chromedriver location
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.indeed.com/')
elem = driver.find_element(By.ID, 'text-input-what')
elem.clear()
elem.send_keys('data scientist')
elem.send_keys(Keys.RETURN)

original_url = driver.current_url
driver.quit()

print(original_url)
