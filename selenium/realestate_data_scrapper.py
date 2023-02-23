from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/rohit/Work/Python/softwares/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

addresses = []
prices = []
urls = []
success_list = []
fail_list = []


def scrape_data_from_daft():
    driver.get("https://www.daft.ie/property-for-sale/ireland?showMap=false")
    #search_results = driver.find_elements(By.CLASS_NAME,"SearchPage__Result-gg133s-2 djuMQD")
    results = driver.find_elements(By.XPATH,'//li[contains(@data-testid, "result-")]')
    # Create empty lists to store the addresses and prices

    for result in results:
        # Find the address and price elements
        # address_element = result.find_element(By.CSS_SELECTOR, 'h2[data-testid="address"]')
        # price_element = result.find_element(By.CSS_SELECTOR, 'h3[class*="TitleBlock__StyledCustomHeading"]')
        address_element = result.find_element(By.XPATH,'.//h2[@data-testid="address"]')
        price_element = result.find_element(By.XPATH,'.//h3[@class="TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq"]')
        property_url_element = result.find_element(By.CSS_SELECTOR,'a[href*="/for-sale/"]')
        url = property_url_element.get_attribute('href')

        # Get the text of the address and price elements
        address = address_element.text
        price = price_element.text

        # Add the address and price to the appropriate lists
        addresses.append(address)
        prices.append(price)
        urls.append(url)

    return addresses, prices, urls


def fill_form_with_scrapped_data():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScM1MrEiKQa5b3VLir9olF34SlkgK2_zSah2I5B_HXmCBAEPg/viewform?usp=sf_link")
    inputs = driver.find_elements(By.TAG_NAME,"input")
    address_input = inputs[0]
    price_input = inputs[1]
    url_input = inputs[2]
    # print(inputs)
    # for n in range(len(inputs)):
    #     input = input[n].find_element(By.TAG_NAME,"input")
    #     input.send_keys(addresses[n])
    # price_input = driver.find_element(By.CLASS_NAME,"//input[@aria-label='Price']")
    # url_input = driver.find_element(By.CLASS_NAME,"//input[@aria-label='Property URL']")

    return address_input, price_input, url_input


def fill_and_submit_form():
    addresses, prices, urls = scrape_data_from_daft()
    address_input, price_input, url_input = fill_form_with_scrapped_data()

    for n in range(3):
        print(addresses[n])
        # try:
        #     address_input.send_keys(addresses[n])
        #     price_input.send_keys(prices[n])
        #     url_input.send_keys(urls[n])
        #
        #     submit_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        #     submit_button.click()
        #
        #     clear_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        #     clear_button.click()
        # except:
        #     fail_list.append(n)
        # finally:
        #     clear_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        #     clear_button.click()


fill_and_submit_form()
# scrape_data_from_daft()
sleep(1)
driver.quit()

# Print the addresses and prices
# print(addresses)
# print(prices)
# print(urls)

