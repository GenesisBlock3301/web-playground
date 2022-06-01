from app.decorators import query_debugger

from app.models import Book, Store, Publisher


@query_debugger
def book_list():
    query_set = Book.objects.all()
    print(len(query_set))
    books = []
    for book in query_set:
        books.append({'id': book.id, "name": book.name,
                     "publisher": book.publisher.name})

    return books


@query_debugger
def book_list_select_related():
    query_set = Book.objects.select_related("publisher").all()
    books = []
    for book in query_set:
        books.append({'id': book.id, "name": book.name,
                     "publisher": book.publisher.name})
    return books


@query_debugger
def store_list():
    query_set = Store.objects.all()

    stores = []
    for store in query_set:
        books = [book.name for book in Book.objects.all()]
        stores.append({'id': store.id, "name": store.name, "books": books})
    return stores


@query_debugger
def store_list_prefetch_related():
    query_set = Store.objects.prefetch_related("books")

    stores = []
    for store in query_set:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, "name": store.name, "books": books})
    return stores
