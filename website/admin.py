from django.contrib import admin
from website.models import Product,AuthUser
from website.models import Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(AuthUser) 