from bs4 import BeautifulSoup
import requests

r = requests.get('http://books.toscrape.com/index.html')
    soup = BeautifulSoup(r.content)

    # Extracting categories
    categories = []
    a_list = soup.select('a[href*="catalogue/category/"]') # Select 'a' tags with links containing categories
    id = 1

    for a in a_list:
        a_href_category = a.get_text(strip=True)
        if a_href_category not in categories:
            categories.append({'id': id, 'name': a_href_category})
            id++