from bs4 import BeautifulSoup
# import lxml
with open("website.html",mode="r") as file:
    html_file = file.read()

soup = BeautifulSoup(html_file,"html.parser")

# print(soup.h3['class'])

all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1",id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)