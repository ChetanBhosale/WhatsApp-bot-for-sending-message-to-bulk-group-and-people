import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = './drive/chromedriver.exe'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(10)

input('Press Enter after scanning QR code')

def send_whatsapp_message(group_name, message):

    search_input = driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
    search_input.click()
    search_input.send_keys(group_name)
    search_input.send_keys(Keys.ENTER)

    # driver.implicitly_wait(10)
    time.sleep(5)
    
    message_input = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_input.click()

    for line in message.split('\n'):
        message_input.send_keys(line)
        message_input.send_keys(Keys.SHIFT + Keys.ENTER)

    message_input.send_keys(Keys.ENTER)
    time.sleep(10)

    print('Message sent successfully.')

group_names = ['King Kay Group Canada']
message = 'Hello\n This is the Test Message'

for group_name in group_names:
    send_whatsapp_message(group_name, message)
    time.sleep(2)