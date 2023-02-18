import requests
from bs4 import BeautifulSoup
import lxml

PRODUCT_NAME = "Epson CO-FH02 Full HD 1080p 3,000 lumen Android TV Projector"
ORIGINAL_PRICE = 800.00
DISCOUNTED_PRICE = ""
AMAZON_PRODUCT_URL = "https://www.amazon.co.uk/gp/product/B0B985SFVD/ref=ox_sc_saved_title_6?smid=A3P5ROKL5A1OLE&psc=1"
MACBOOK_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}
msg_str = ""


def get_product_price(amazon_product_url,headers):
    amazon_product_html = requests.get(
        amazon_product_url, headers=headers, verify=False, timeout=10).content
    soup = BeautifulSoup(amazon_product_html, "lxml")
    price = soup.find(id="corePrice_feature_div").get_text().split("£")[1]
    return float(price)


def is_price_discounted(product_price, original_price):
    if ((original_price - product_price)/original_price * 100) < 20.00:
        print("Product Not Discounted")
        exit()
    else:

        generate_letter(PRODUCT_NAME,AMAZON_PRODUCT_URL,ORIGINAL_PRICE,product_price,EMAIL_TEMPLATE)



def main():
    print("Hello World!")
    product_price=get_product_price(AMAZON_PRODUCT_URL,MACBOOK_HEADERS)
    is_price_discounted(product_price,ORIGINAL_PRICE)

if __name__ == "__main__":
    main()