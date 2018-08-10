'''base/views.py'''
from django.http import HttpResponse
from apps.scraper.models import Category, Book
from apps.scraper.scrape import scrape

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
        html += '<tr><td><button type="button">Delete</button></td>'
        html += '<td>' + str(book.id) + '</td>'
        category_name = categories.get(id=book.category_id).name
        html += '<td>' + category_name + '</td><td>' + str(book.category_id) + '</td>'
        html += '<td>' + book.title + '</td>'
        html += '<td>' + book.thumbnail_url + '</td>'
        html += '<td>' + book.price + '</td>'
        html += '<td>' + 'True' if book.stock else 'False' + '</td>'
        html += '<td>' + book.product_description + '</td>'
        html += '<td>' + book.upc + '</td></tr>'

    html += '</tbody></table>'
    return HttpResponse(html)
