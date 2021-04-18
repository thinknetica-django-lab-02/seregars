from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    image = ImageField(null=True, upload_to='main/static/images/goods')

    def __str__(self):
        return self.title


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500, null=True)
    birth_date = models.DateField(default=datetime.today)
    avatar = ImageField(null=True, upload_to='main/static/images/users')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile')
