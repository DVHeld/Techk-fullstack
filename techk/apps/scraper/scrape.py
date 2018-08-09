from bs4 import BeautifulSoup
import requests


def scrape():
    '''Description
    The scrape() function scrapes http://books.toscrape.com/index.html and returns a dictionary
    with two entries, categories and books, both containing data scraped from the mentioned website.

    Syntax
    scrape()

    Parameters:
    This function takes no parameters.

    Return Value
    This function returns a dictionary returns with two entries with the keys "categories" and "books",
    each of which contains a list of dictionaries. The "categories" entry contains a list of
    dictionaries, each containing the keys "id" and "name". The "books" entry contains a list of
    dictionaries, each containing the keys "id", "category_id", "title", "thumbnail_url", "price", "stock",
    "product_description", and "upc".
    
    Example
    The following example shows the usage of the scrape() function:
    
    result = scrape()
    print result
    
    When run, the above program produces a result similar to the following, depending on the contents on the aforementioned website:
    
    [{
        "categories": [
            {
                "id": 1,
                "name": "Travel"
            }, {
                "id": 2,
                "name": "Mystery"
            }, {
                "id": 3,
                "name": "Historical Fiction"
            }
        ],
        "books": [
            {
                "id": 1;
                "category_id": 1,
                "title": "It's Only the Himalayas",
                "thumbnail_url": "http://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg",
                "price": "£45.17",
                "stock": true,
                "product_description": "Wherever you go, whatever you do, just ...",
                "upc": "a22124811bfa8350"
            }
        ]
    }]'''

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