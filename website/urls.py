from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include


urlpatterns = [
    # Token authentication
    path('token/', obtain_auth_token, name='api_token_auth'),

    # Product APIs
    path('products/', views.product_list, name='product-list'),  # API (JSON)
    path('products/page/', views.product_page, name='product-page'),
    path('products/add/', views.add_product, name='add-product'),
    path('products/update/<int:pk>/', views.update_product, name='update-product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete-product'),

    # Login
    path('login/', views.user_login, name='user-login'),
    path('log/', views.log, name='log'),

    # Dashboard
    path('dashboard/', views.dashboard_stats, name='dashboard-stats'),

    # Cart URLs
    path('cart/', views.view_cart, name='view-cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),

    # Include other API urls
    path('api1/', include('website.api.urls')),
]
