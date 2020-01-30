import requests
from bs4 import BeautifulSoup


people = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
people_json  = people.json()
B = people_json["bpi"]["USD"]["rate"]
print("Bitcoin Price: "+ B + people_json["bpi"]["USD"]["description"])

page = requests.get("https://www.tgju.org/chart/price_dollar_rl")
soup = BeautifulSoup(page.content, 'html.parser')
D = soup.find("span", itemprop="price").get_text()
print("Dolar Price :" + D + " Rials")



