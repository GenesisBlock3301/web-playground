from django.contrib import admin
from app.models import Book, Country, City, Publisher, Store

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
