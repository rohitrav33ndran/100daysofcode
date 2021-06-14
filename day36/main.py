import requests
from datetime import date, timedelta
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_no = os.environ['TWILIO_PHONE_NO']
clien_phone_no = os.environ['CLIENT_PHONE_NO']

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey":STOCK_API_KEY
}

NEWS_PARAMS = {
    "q": STOCK,
    "apiKey": NEWS_API_KEY,
}



def get_news():
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_data = news_response.json()['articles']
    top_news_list = []
    for news in news_data[:3]:
        top_news_list.append({
            news['title']: news['description']
        })
    return top_news_list


def send_sms(news_list, downtext):
    for news in news_list:
        for k,v in news.items():
            client = Client(twilio_account_sid, twilio_auth_token)
            message = client.messages \
                .create(
                body=f"{STOCK}: {downtext} Headline: {k} Brief: {v}",
                from_=twilio_phone_no,
                to=clien_phone_no
            )
            print(message.status)

today = date.today()
yesterday = today - timedelta(days = 3)
day_before_yesterday = today - timedelta(days = 4)

response = requests.get(url=STOCK_ENDPOINT,params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]

yesterday_stock_dict = data[str(yesterday)]
day_before_yesterday_stock_dict = data[str(day_before_yesterday)]

y_close = float(yesterday_stock_dict['4. close'])
d_y_close = float(day_before_yesterday_stock_dict['4. close'])
diff = abs(y_close - d_y_close)

perc_y_close = (y_close * 5) / 100

if diff > perc_y_close:
    down_text = "🔻5%"
    news_list = get_news()
    send_sms(news_list, down_text)



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

