from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include('website.urls')),

    # Default → login page
    path('', views.log, name='login'),

    # Home page after login
    path('home/', views.index, name='home'),

    # Product + Cart
    path('products/page/', views.product_page, name='product-page'),
    path('products/add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.view_cart, name='view-cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),
]
