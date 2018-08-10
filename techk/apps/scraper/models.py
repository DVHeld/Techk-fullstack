'''scraper app models'''
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    '''Django model for scraped categories'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Book(models.Model):
    '''Django model for scraped books'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    thumbnail_url = models.URLField()
    price = models.CharField(max_length=16)
    stock = models.NullBooleanField()
    product_description = models.CharField(max_length=1024)
    upc = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) + ' - ' + self.title + ' - ' + str(self.category)
