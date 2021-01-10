from bs4 import BeautifulSoup

import requests

url = "http://mydiba.me/"
site_data = requests.get(url)
#soup = BeautifulSoup(site_data.content, 'html.parser')
#imgs = soup.find_all("img",class_="<img src="http://mydiba.me/wp-content/uploads/q1epO0eO8DWu8Vo8tPfvVlzW48T-320x465.jpg")
#print(imgs)