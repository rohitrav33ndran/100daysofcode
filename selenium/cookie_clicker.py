from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/rohit/Work/Python/softwares/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.CSS_SELECTOR,"#cookieAnchor button")

while True:
    cookie.click()

driver.quit()