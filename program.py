import time
import requests
from bs4 import BeautifulSoup


def get_product_info(query):
    ans = query.replace(" ","+")
    url = f'https://www.amazon.pl/s?k={ans}'
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        item = soup.select('div.a-section.a-spacing-base')[0]
        rating_element = item.select('span.a-icon-alt')[0]
        if rating_element:
            rating = rating_element.text
        else:
            rating = "Brak oceny"
        name_element = item.select('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')[0]
        if name_element:
            name = name_element.text
        else:
            name = "Brak nazwy"
        price_element = item.select('span.a-price span.a-offscreen')[0].get_text()
        if price_element:
            price = price_element
        else:
            price = "Brak ceny"
        return name, rating, price
    except:
        print("Ponowna próba znalezienia produktu")
        time.sleep(5)
        return get_product_info(query)
       
def main():
    query = input("Podaj nazwę produktu: ")
    name, rating, price = get_product_info(query)
    print('Nazwa produktu:', name)
    print('Cena produktu:', price)
    print('Ocena produktu:', rating)

main()