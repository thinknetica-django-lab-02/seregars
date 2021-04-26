from datetime import datetime
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from sorl.thumbnail import ImageField

from shop.settings import MEDIA_ROOT


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
    image = ImageField(null=True, upload_to=f'{MEDIA_ROOT}images/goods')

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
    avatar = ImageField(null=True, upload_to=f'{MEDIA_ROOT}/images/users')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='common_users'))
        send_mail("Добро пожаловать", "Вы зарегистрировались", 'from@example.com', [instance.email],
                  html_message='<html><body><h1>Добро пожаловать!</h1></body></html>')