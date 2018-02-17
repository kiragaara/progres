from bs4 import BeautifulSoup
import requests




r = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
soup = BeautifulSoup(r.content,"html.parser")

print(soup.title.string)
