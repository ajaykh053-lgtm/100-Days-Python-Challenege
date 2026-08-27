import requests
from bs4 import BeautifulSoup
from pprint import pprint
# respones = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
# soup_static_web = BeautifulSoup(respones.text,'html.parser')
# a_tag = soup_static_web.find_all(name="a", class_="storylink")
result =  requests.get(url="https://news.ycombinator.com/news")
soup_live_web = BeautifulSoup(result.text,'html.parser')
span_tag = soup_live_web.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
# for name in a_tag:
#     text = name.string
#     article_texts.append(text)
#     link = name.get("href")
#     article_texts.append(link)
for name in span_tag:
    text = name.find(name="a").getText()
    # pprint(text)
    article_texts.append(text)
    link = name.find(name="a").get("href")
    # pprint(link)
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup_live_web.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)
largest_number = max(article_upvotes)
# print(largest_number)
largest_index = article_upvotes.index(largest_number)
# print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])


# This is gonna give me the mosted voted news in hacker news top 30 News





























































# with open(file="day45/bs4-start/website.html" , mode="r") as file:
#     content = file.read()
#     # print(content)

# soup = BeautifulSoup(content,'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading =  soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.name)
# print(section_heading.getText())
# print(section_heading.get('class'))

# company_url = soup.select_one("p a")
# print(company_url)

# name  =  soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)