from __future__ import print_function
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name



class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    class Meta:
        default_related_name = "books"
    
    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(to=Book)

    class Meta:
        default_related_name = "stores"
    
    def __str__(self) -> str:
        return self.name