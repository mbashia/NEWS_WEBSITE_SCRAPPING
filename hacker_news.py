from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

url = "https://thehackernews.com/"
now = datetime.now()
# timedelta class in datetime module is used to represent a duration between two dates or times
start_date = now - timedelta(days=2)
# while True: for looping through different pages of the website
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
news = soup.find_all("div", class_="body-post clear")
for item in news:
    heading = item.find("h2", class_="home-title").text.strip()
    link = item.find("a", class_="story-link").attrs["href"]
    # we use the try and except block for when the date and new_type values are none
    try:
        date = item.find("span", class_="h-datetime").text
    except:
        date = ""
    try:
        news_type = item.find("span", class_="h-tags").text
    except:
        news_type = ""
    # print(heading)
    # print(link)
    # print(date)
    # print(news_type)
    # print("\n")

    news_info = f'''\n       heading:{heading}
       link:{link}
       date:{date}
       news_type:{news_type}\n
    \n
       
       
       
        
                '''

    edited_news = news_info.rstrip()
    with open('news.txt', "a", encoding="utf-8") as f:
        f.write(edited_news)

# # fetching data from all pages of the website
# url = soup.find("a", class_="blog-pager-older-link-mobile").attrs['href']
# if not url:
#     break
