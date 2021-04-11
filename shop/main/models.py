from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def __str__(self):
        return self.title


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    instance.profile.save()
