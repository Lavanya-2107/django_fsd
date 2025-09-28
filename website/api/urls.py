from django.urls import path,include
from django.contrib import admin
from website.api import views

urlpatterns=[
      path('products/', views.product_list, name='product-list'),
      path('products/add/', views.add_product, name='add-product'),
      path('products/update/<int:pk>/', views.update_product, name='update-product'),
      path('login/', views.user_login, name='user-login'),
      path('products/delete/<int:pk>/', views.delete_product, name='delete-product'), 
      path('dashboard/', views.dashboard_stats, name='dashboard-stats')
]