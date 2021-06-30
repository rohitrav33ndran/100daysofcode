from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")

# all_titles = soup.find_all(name="a",class_="storylink")

# all_titles = soup.find_parent(name="a")
# for title in all_titles:
#     print(title.getText())
#     print(title.get('href'))

article_text = []
article_link = []
articles = soup.find_all(name="a",class_="storylink")
for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get('href')
    article_link.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
print(len(article_text))

max_score = max(article_upvotes)
print(max_score)
max_index_score = article_upvotes.index(max_score)
print(max_index_score)

print(article_text[max_index_score + 1])
print(article_link[max_index_score + 1])
