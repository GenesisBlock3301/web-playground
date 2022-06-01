import random
from unicodedata import name
from django.core.management.base import BaseCommand
from app.models import Publisher,Store,Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # create 5 publisher
        publishers = [Publisher(name=f"publisher{index}") for index in range(1,6)]
        Publisher.objects.bulk_create(publishers)

        # create 20 books
        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter += 1
                books.append(Book(name=f"Book{counter}",price=random.randint(50,300),publisher=publisher))
        Book.objects.bulk_create(books)

        # create 10 store and insert 10 books in every store
        books = list(Book.objects.all())
        for i in range(10):
            temp_book = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_book)
            store.save()