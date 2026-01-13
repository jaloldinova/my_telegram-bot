from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.customer.name
