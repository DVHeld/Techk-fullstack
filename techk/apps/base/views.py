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
    html += '<table><thead><td>ID</td><td>Name</td></thead><tbody>'
    categories = Category.objects.all()
    if categories:
        for category in categories:
            html += '<tr><td><a href="">' + str(category.id) + '</a></td><td><a href="">'
            html += category.name + '</a></td></tr>'
    html += '</tbody></table>'

    html += '</td></br><h1>==========Books==========</h1></br>'
    html += '<table><thead><td></td><td>ID</td><td>Category Name</td><td>Category ID</td><td>Title'
    html += '</td><td>Thumbnail URL</td><td>Price</td><td>Stock</td><td>Description</td><td>UPC'
    html += '</td></thead><tbody>'
    books = Book.objects.all()
    for book in books:
        #html += '</br>=============================='
        #html += '</br></br>========= ID =========</br>'
        html += '<tr><td><button type="button">Delete</button></td>'
        html += '<td>' + str(book.id) + '</td>'
        #html += '</br></br>========= Category =========</br>'
        category_name = categories.get(id=book.category_id).name
        html += '<td>' + category_name + '</td><td>' + str(book.category_id) + '</td>'
        #html += '</br></br>========= Title =========</br>'
        html += '<td>' + book.title + '</td>'
        #html += '</br></br>========= Thumbnail =========</br>'
        html += '<td>' + book.thumbnail_url + '</td>'
        #html += '</br></br>========= Price =========</br>'
        html += '<td>' + book.price + '</td>'
        #html += '</br></br>========= Stock =========</br>'
        html += '<td>' + 'True' if book.stock else 'False' + '</td>'
        #html += '</br></br>========= Description =========</br>'
        html += '<td>' + book.product_description + '</td>'
        #html += '</br></br>========= UPC =========</br>'
        html += '<td>' + book.upc + '</td></tr>'
    
    html += '</tbody></table>'

    # Placeholder html etc
    html += '<center></br></br>=== END ===</br></br><img src="http://juliareda.eu/wp-content/uploa'
    html += 'ds/2015/10/20619_8_bit_all_your_base_are_belong_to_us-1440x486.jpg" alt="CATS" width='
    html += '"1300"></br>All your base are belong to us.</br>You have no chance to survive make yo'
    html += 'ur time.</center>'

    return HttpResponse(html)
