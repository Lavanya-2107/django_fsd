# # from django.db import models
# # from django.contrib.auth.models import User,AbstractUser

# # class Product(models.Model):
# #     name = models.CharField(max_length=250)
# #     description = models.TextField()
# #     price = models.DecimalField(max_digits=10, decimal_places=2)

# #     def __str__(self):
# #         return self.name

# # class Order(models.Model):
# #     order_date = models.DateField()
# #     delivery_date = models.DateField()
# #     itemname = models.CharField(max_length=250)

# #     def __str__(self):
# #         return self.itemname

# # # Optional: Customer model if you want separate profile info
# # class Customer(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     phone = models.CharField(max_length=20, blank=True)

# #     def __str__(self):
# #         return self.user.username
# # class AuthUser(AbstractUser):
# #     email=models.EmailField(unique=True)
# #     username=models.CharField(max_length=150,unique=True)
# #     user_permissions = None
# #     groups=None
# #     first_name=None
# #     last_name=None
# #     def __str__(self):
# #         return self.email   


# from django.db import models
# from django.contrib.auth.models import User, AbstractUser
# from django.conf import settings   # <-- add this
# from django.dispatch import receiver
# from django.db.models.signals import post_save 

# class Product(models.Model):
#     name = models.CharField(max_length=250)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     order_date = models.DateField()
#     delivery_date = models.DateField()
#     itemname = models.CharField(max_length=250)

#     def __str__(self):
#         return self.itemname
# @receiver(post_save,sender='website.Authuser')
# def create_auth_user_token(sender,instance,created,**kwargs):
#     if created:
#         from rest_framework.authtoken.models import Token
#         Token.objects.create(user=instance)
# # Optional: Customer model if you want separate profile info
# class Customer(models.Model):
#     # ⬇️ change only this line
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return self.user.username


# class AuthUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     user_permissions = None
#     groups = None
#     first_name = None
#     last_name = None

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save   # <-- must import this

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    itemname = models.CharField(max_length=250)

    def __str__(self):
        return self.itemname

# Optional: Customer model
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # <-- keep this
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class AuthUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    user_permissions = None
    groups = None
    first_name = None
    last_name = None

    def __str__(self):
        return self.email

# Signal to create token automatically
@receiver(post_save, sender=AuthUser)   # <-- must be class, not string
def create_auth_user_token(sender, instance, created, **kwargs):
    if created:
        from rest_framework.authtoken.models import Token
        Token.objects.create(user=instance)

