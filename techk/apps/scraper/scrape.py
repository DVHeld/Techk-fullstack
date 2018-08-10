'''scraper/scrape.py'''
from bs4 import BeautifulSoup
import requests
from .models import Category, Book

def scrape():
    '''Scrapes http://books.toscrape.com/index.html and stores the retrieved data
    in the database.'''

    clear_tables()

    base_url = 'http://books.toscrape.com/'
    req = requests.get(base_url + 'index.html')
    soup = BeautifulSoup(req.content, 'html.parser')

    categories = get_categories(soup)
    Category.objects.bulk_create(categories)
    categories = Category.objects.all()
    books = get_books(soup, categories, base_url)
    Book.objects.bulk_create(books)

def clear_tables():
    '''Clears all tables of previous data.'''

    categories = Category.objects.all()
    if categories:
        categories.delete()
    books = Book.objects.all()
    if books:
        books.delete()

def get_categories(soup):
    '''Obtains categories from soup and returns them in a list.'''

    categories = []
    anchor_list = soup.select('a[href*="catalogue/category/"]')

    for anchor in anchor_list:
        a_href_category = anchor.get_text(strip=True)
        if a_href_category not in categories:
            categories.append(Category(name=a_href_category))

    return categories

def get_books(soup, categories, base_url):
    '''Obtains books from soup and returns them in a list.'''
    books = []
    book_list = soup(class_='product_pod')

    for book in book_list:
        book_url = base_url + book.find('a')['href']
        r_book = requests.get(book_url)
        soup_book = BeautifulSoup(r_book.content, 'html.parser')
        book_category = soup_book.select('a[href*="category/books/"]')[0].get_text(strip=True)

        for category in [cat for cat in categories if cat.name == book_category]:
            book_category_id = category.id

        book_title = soup_book.find(class_='product_main').h1.get_text(strip=True)
        book_thumbnail = base_url + soup_book.find('img')['src'][6:]
        book_price = soup_book.find(class_='price_color').get_text(strip=True)
        availability = soup_book.find(class_='instock availability').get_text(strip=True)[:8]
        book_stock = True if availability == 'In stock' else False
        soup_description = soup_book.find(id='product_description').find_next_sibling('p')
        book_description = soup_description.get_text(strip=True)
        book_upc = soup_book.find('td').get_text(strip=True)

        books.append(Book(
            category_id=book_category_id,
            title=book_title,
            thumbnail_url=book_thumbnail,
            price=book_price,
            stock=book_stock,
            product_description=book_description,
            upc=book_upc
        ))

    return books
