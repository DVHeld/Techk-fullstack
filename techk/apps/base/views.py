'''View for base app.'''
'''base/views.py'''
from django.http import HttpResponse
from apps.scraper.models import Category, Book
from apps.scraper.scrape import scrape
#from django.apps import apps

def index(request):
    '''
    Main and only view. Shows web menu and presents data.
    '''
    scrape()
    html = ''

    html += '<h1>==========Categories==========</h1></br>'
    categories = Category.objects.all()
    if categories:
        for category in categories:
            html += '</br>' + category.name + ': ' + str(category.id)

    html += '</br></br><h1>==========Books==========</h1></br>'
    books = Book.objects.all()
    for book in books:
        html += '</br>=============================='
        html += '</br></br>========= ID =========</br>'
        html += str(book.id)
        html += '</br></br>========= Category =========</br>'
        category_name = categories.get(id=book.category_id).name
        html += category_name + ': ' + str(book.category_id)
        html += '</br></br>========= Title =========</br>'
        html += book.title
        html += '</br></br>========= Thumbnail =========</br>'
        html += book.thumbnail_url + '</br></br>' + '<img src="' + book.thumbnail_url + '">'
        html += '</br></br>========= Price =========</br>'
        html += book.price
        html += '</br></br>========= Stock =========</br>'
        html += 'true' if book.stock else 'false'
        html += '</br></br>========= Description =========</br>'
        html += book.product_description
        html += '</br></br>========= UPC =========</br>'
        html += book.upc + '</br>'

    # Placeholder html etc
    html += '<center></br></br>=== END ===</br></br><img src="http://juliareda.eu/wp-content/uploa'
    html += 'ds/2015/10/20619_8_bit_all_your_base_are_belong_to_us-1440x486.jpg" alt="CATS" width='
    html += '"1300"></br>All your base are belong to us.</br>You have no chance to survive make yo'
    html += 'ur time.</center>'

    return HttpResponse(html)
