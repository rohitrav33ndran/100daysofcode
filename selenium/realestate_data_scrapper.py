from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/rohit/Work/Python/softwares/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

addresses = []
prices = []
urls = []

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


def fill_form_with_scrapped_data():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScM1MrEiKQa5b3VLir9olF34SlkgK2_zSah2I5B_HXmCBAEPg/viewform?usp=sf_link")

    inputs = driver.find_elements(By.CLASS_NAME,"whsOnd zHQkBf")
    # for n in range(len(inputs)):
    #     input = input[n].find_element(By.TAG_NAME,"input")
    #     input.send_keys(addresses[n])
    # price_input = driver.find_element(By.CLASS_NAME,"//input[@aria-label='Price']")
    # url_input = driver.find_element(By.CLASS_NAME,"//input[@aria-label='Property URL']")


driver.quit()

# Print the addresses and prices
print(addresses)
print(prices)
print(urls)
