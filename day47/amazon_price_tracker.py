import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}

AMAZON_URL = "https://www.amazon.co.uk/gp/product/B0B985SFVD/ref=ox_sc_saved_title_6?smid=A3P5ROKL5A1OLE&psc=1"
amazon_product_html = requests.get(AMAZON_URL, headers=HEADERS, verify=False, timeout=10).text

soup = BeautifulSoup(amazon_product_html,"lxml")

print(soup)
