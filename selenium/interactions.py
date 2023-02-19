from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/rohit/Work/Python/softwares/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics_count = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
print(statistics_count.text)
driver.quit()