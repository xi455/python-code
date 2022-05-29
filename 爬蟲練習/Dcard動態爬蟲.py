from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver.exe')
driver.get('https://www.dcard.tw/f')

search = driver.find_element_by_name('query')
search.clear()
search.send_keys('比特幣')
search.send_keys(Keys.RETURN)

WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,'sc-3yr054-1'))
)

titles=driver.find_elements_by_class_name('tgn9uw-3')
for i in titles:print(i.text)

link=driver.find_element_by_link_text('我可能從詐騙手上賺到了976元')
link.click()
driver.back()
driver.back()
driver.forward()

time.sleep(3)
driver.quit()