from django.contrib import admin
from django.urls import path, include
from app.views import Book_list,index
urlpatterns = [
    path('book_list/', Book_list, name="book_list"),
    path('index/', index, name="index"),
]
