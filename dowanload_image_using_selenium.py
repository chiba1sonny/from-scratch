#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import driver

#Opens up web driver and goes to Google Images
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

box = driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('Mongolian Ger')
box.send_keys(Keys.ENTER)

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

# //*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img

for i in range(1,100):
    try:
        driver.find_element("xpath",'//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('customdata\ger ('+str(i)+').png')
    except:
        pass
