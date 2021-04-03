from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Tags(models.Model):
    title = models.CharField(max_length=100)


class Seller(models.Model):
    name = models.CharField(max_length=200)
