from bs4 import BeautifulSoup
import requests

r = requests.get('http://books.toscrape.com/index.html')
    soup = BeautifulSoup(r.content)

    #with open('http://books.toscrape.com/index.html') as fp:
    #   soup = BeautifulSoup(fp)
    #html += soup

    # Extracting categories
    categories = []
    a_list = soup.select('a[href*="catalogue/category/"]') # Select 'a' tags with links containing categories
    html = ''

    for a in a_list:
        a_href_category = a.get_text().strip()
        if a_href_category not in categories:
            categories.append(a_href_category)