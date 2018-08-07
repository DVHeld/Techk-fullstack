from bs4 import BeautifulSoup
import requests


def scrape():
    """
    """
    base_url = 'http://books.toscrape.com/'
    r = requests.get(base_url + 'index.html')
    soup = BeautifulSoup(r.content)

    categories = []
    a_list = soup.select('a[href*="catalogue/category/"]')
    id = 1

    for a in a_list:
        a_href_category = a.get_text(strip=True)
        if a_href_category not in categories:
            categories.append({'id': id, 'name': a_href_category})
            id += 1

    books = []
    book_list = soup(class_='product_pod')
    id = 1

    for book in book_list:
        book_url = base_url + book.find('a')['href']
        r_book = requests.get(book_url)
        soup_book = BeautifulSoup(r_book.content)

        book_category = soup_book.select('a[href*="category/books/"]')[0].get_text(strip=True)

        for category in [x for x in categories if x['name'] == book_category]:
            book_category_id = category['id']
            break
        
        book_title = soup_book.find(class_='product_main').h1.get_text(strip=True)
        book_thumbnail = base_url + soup_book.find('img')['src'][6:]
        book_price = soup_book.find(class_='price_color').get_text(strip=True)
        book_stock = True if soup_book.find(class_='instock availability').get_text(strip=True)[:8] == 'In stock' else False
        book_description = soup_book.find(id='product_description').find_next_sibling('p').get_text(strip=True)
        book_UPC = soup_book.find('td').get_text(strip=True)

        books.append({
            'id': id
            , 'category_id': book_category_id
            , 'title': book_title
            , 'thumbnail_url': book_thumbnail
            , 'price': book_price
            , 'stock': book_stock
            , 'product_description': book_description
            , 'upc': book_UPC
        })
        id += 1

    return {'categories': categories, 'books': books}