from django.urls import path
from . import views

urlpatterns = [
    # Product APIs
    path('products/', views.product_list, name='product-list'),
    path('products/add/', views.add_product, name='add-product'),
    path('products/update/<int:pk>/', views.update_product, name='update-product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete-product'),

    # Login
    path('login/', views.user_login, name='user-login'),
    path('log/', views.log, name='log'),

    # Dashboard
    path('dashboard/', views.dashboard_stats, name='dashboard-stats'),

    # Cart
    path('cart/', views.view_cart, name='view-cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),

    # Log event endpoint
    path('log-event/', views.log_event, name='log-event'),
]
