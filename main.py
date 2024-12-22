import requests

url = "https://coinmarketcap.com"

response = requests.get(url)

if response.status_code == 200:
    print("Успешно подключились к сайту")
else:
    print("Ошибка подключения", response.status_code)

from bs4 import BeautifulSoup
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title_tag = soup.find("title")

rows = soup.findAll("tr")

for row in rows[1: 11]:
    name_tag = row.find("p", class_="sc-65e7f566-0 byYAWx coin-item-symbol")
    price_tag = row.find("div", class_="sc-b3fc6b7-0 dzgUIj")
    hour_tag = row.find("span", class_="sc-a59753b0-0 ivvJzO")
    twentyfourhour_tag = row.find("span", class_="sc-a59753b0-0 ivvJzO")
    sevendays_tag = row.find("span", class_="sc-a59753b0-0 ivvJzO")
    marketcap_tag = row.find("span", class_="sc-11478e5d-0 chpohi")

    print(f"Крипта: {name_tag.text}, Цена: {price_tag.text}, Изменения за последний час: {hour_tag.text}, Изменения за последние 24 часа: {twentyfourhour_tag.text},"
          f" Изменения за последние 7 дней: {sevendays_tag.text},"
          f" Рыночная стоимость: {marketcap_tag.text}")