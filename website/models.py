from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# -------------------------------
# Custom User
# -------------------------------
class AuthUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Automatically create auth token for each new user
@receiver(post_save, sender=AuthUser)
def create_auth_user_token(sender, instance, created, **kwargs):
    if created:
        from rest_framework.authtoken.models import Token
        Token.objects.create(user=instance)

# -------------------------------
# Product Model
# -------------------------------
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# -------------------------------
# Order Model
# -------------------------------
class Order(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    itemname = models.CharField(max_length=250)

    def __str__(self):
        return self.itemname

# -------------------------------
# Customer Model
# -------------------------------
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
