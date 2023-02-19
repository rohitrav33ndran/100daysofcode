from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/rohit/Work/Python/softwares/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get("https://www.amazon.co.uk")
# driver.get("https://www.amazon.co.uk/Epson-CO-FH02-1080p-Android-Projector/dp/B0B985SFVD/?_encoding=UTF8&pd_rd_w=TED7G&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=MXXV24412G65W0X3EQXT&pd_rd_wg=9qfIC&pd_rd_r=0cf64307-2b7d-4f23-97a1-baa8ce58cc62&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
# price=driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(price.text)

driver.get("https://python.org")
# data = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]')
# print(data.text)

# datas = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# # datas = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
# for time in datas:
#     print(time.text)

# datas = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
# for data in datas:
#     print(data.text)

event_times = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
events = {}
for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }

print(events)

driver.quit()

