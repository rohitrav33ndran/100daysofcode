import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

PRODUCT_NAME = "Epson CO-FH02 Full HD 1080p 3,000 lumen Android TV Projector"
ORIGINAL_PRICE = 800.00
DISCOUNTED_PRICE = ""
AMAZON_PRODUCT_URL = "https://www.amazon.co.uk/gp/product/B0B985SFVD/ref=ox_sc_saved_title_6?smid=A3P5ROKL5A1OLE&psc=1"
EMAIL_TEMPLATE = "price_checker_email_template.txt"
EMAIL = os.environ.get("MY_TEST_GMAIL")
EMAIL_PASS = os.environ.get("MY_TEST_GMAIL_PASS")
SMTP_HOST = os.environ.get("GMAIL_SMTP")
SMTP_PORT = os.environ.get("GMAIL_SMTP_PORT")
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


# def send_mail(msg):
#     with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as conn:
#         conn.login(user=EMAIL, password=EMAIL_PASS)
#         conn.connect(host=SMTP_HOST, port=SMTP_PORT)
#         conn.starttls()
#         conn.login(user=EMAIL, password=EMAIL_PASS)
#         conn.sendmail(
#             from_addr=EMAIL,
#             to_addrs=EMAIL,
#             msg="Subject: Amazon Product Price Change\n\n"
#                 f"{msg}"
#         )

# def send_mail(msg):
#     with smtplib.SMTP('smtp.gmail.com', 587) as conn:
#         conn.connect('smtp.gmail.com',587)
#         conn.ehlo()
#         conn.starttls()
#         conn.ehlo()
#         conn.login(user=EMAIL, password=EMAIL_PASS)
#         conn.sendmail(
#             from_addr=EMAIL,
#             to_addrs=EMAIL,
#             msg="Subject: Amazon Product Price Change\n\n"
#                 f"{msg}"
#         )

def send_mail(msg):
    SCOPES = [
            "https://www.googleapis.com/auth/gmail.send"
        ]
    flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText('This is the body of the email')
    message['to'] = 'recipient@gmail.com'
    message['subject'] = 'Email Subject'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None

def generate_letter(product_name, product_url, original_price, discounted_price, email_template):
    global msg_str
    with open(file=f"{email_template}", mode="r") as file:
        for line in file:
            if "[PRODUCT_NAME]" in line:
                msg_str = msg_str + line.replace("[PRODUCT_NAME],", product_name)
                msg_str = msg_str + "\n"
            elif "[ORIGINAL_PRICE]" in line:
                msg_str = msg_str + line.replace("[ORIGINAL_PRICE],", original_price)
                msg_str = msg_str + "\n"
            elif "[DISCOUNTED_PRICE]" in line:
                msg_str = msg_str + line.replace("[DISCOUNTED_PRICE],", discounted_price)
                msg_str = msg_str + "\n"
            elif "[PRODUCT_URL]" in line:
                msg_str = msg_str + line.replace("[PRODUCT_URL],", product_url)
                msg_str = msg_str + "\n"
            else:
                msg_str = msg_str + line + "\n"
    send_mail(msg_str)


def main():
    print("Hello World!")
    product_price=get_product_price(AMAZON_PRODUCT_URL,MACBOOK_HEADERS)
    is_price_discounted(product_price,ORIGINAL_PRICE)

if __name__ == "__main__":
    main()