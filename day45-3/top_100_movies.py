from bs4 import BeautifulSoup
import requests
import regex as re

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text

# soup = BeautifulSoup(response.text,"html.parser")
# # print(soup.prettify())
# headers = soup.find(name="div",class_="jsx-3821216435 listicle-item")
# # print(headers)
#
# header1 = soup.select_one(selector=".jsx-3821216435.listicle-item.h3")
# print(header1)

soup = BeautifulSoup(response, 'html.parser')

movies = re.findall(r'\"titleText\":\"(.*?)\"', str(soup.find(name="body")), re.IGNORECASE)[1:]

movies[99] = "1) " + movies[99]
movies = movies[::-1]
print(movies)