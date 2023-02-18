import base64
import requests
import urllib3
from bs4 import BeautifulSoup
import lxml
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

PRODUCT_NAME = "Epson CO-FH02 Full HD 1080p 3,000 lumen Android TV Projector"
ORIGINAL_PRICE = 500.00
DISCOUNTED_PRICE = ""
AMAZON_PRODUCT_URL = "https://www.amazon.co.uk/gp/product/B0B985SFVD/ref=ox_sc_saved_title_6?smid=A3P5ROKL5A1OLE&psc=1"
MACBOOK_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/16.1 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}
msg_str = ""


def get_product_price(amazon_product_url, headers):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    amazon_product_html = requests.get(
        amazon_product_url, headers=headers, verify=False, timeout=10).content
    soup = BeautifulSoup(amazon_product_html, "lxml")
    price = soup.find(id="corePrice_feature_div").get_text().split("£")[1]
    return float(price)


def is_price_discounted(product_price, original_price):
    # Checking if product is dropped by 20% from original price
    if ((original_price - product_price) / original_price * 100) < 20.00:
        print("Product Not Discounted")
        return False
    else:
        return True


def create_message(sender, to, subject, product_name, product_url, original_price, current_price):
    message = MIMEMultipart()
    # message = MIMEText(message_text)
    body = (
        f"Hi,\n\n"
        f"Amazon has dropped the price of {product_name} from original price £{original_price} to £{current_price}\n\n"
        f"Amazon Link to the product {product_url}.\n\n"
        f"Rohit"
    )
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)


def main():
    print("Hello World!")
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    product_price = get_product_price(AMAZON_PRODUCT_URL, MACBOOK_HEADERS)
    is_discounted = is_price_discounted(product_price, ORIGINAL_PRICE)
    if is_discounted:
        message = create_message('me', 'iamrohitraveendran@gmail.com', 'hello', PRODUCT_NAME, AMAZON_PRODUCT_URL,
                                 ORIGINAL_PRICE, product_price)
        send_message(service=service, user_id='me', message=message)
    else:
        print("Its not discounted. No email sent")


if __name__ == "__main__":
    main()
