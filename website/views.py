from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order
from .serializers import ProductSerializer
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# ----- Home page -----
def index(request):
    return render(request, "website/index.html")

# ----- Products API -----
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# ----- Products page HTML -----
def product_page(request):
    products = Product.objects.all()
    cart = request.session.get('cart', [])
    return render(request, 'website/product.html', {'products': products, 'cart': cart})

# ----- Add to cart -----
def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect('product-page')

# ----- View cart -----
def view_cart(request):
    cart = request.session.get('cart', [])
    cart_items = Product.objects.filter(id__in=cart)
    return render(request, 'website/common/cart.html', {'cart_items': cart_items})

# ----- Remove from cart -----
def remove_from_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
        request.session['cart'] = cart
    return redirect('view-cart')

# ----- Add product API -----
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- Update product API -----
@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- Delete product API -----
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)

# ----- HTML login -----
def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        return render(request, 'website/login.html', {'error': 'Invalid username or password'})
    return render(request, 'website/login.html')

# ----- REST login API -----
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        auth_login(request, user)
        return Response({"message": "Login successful"})
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# ----- Dashboard stats -----
@api_view(['GET'])
def dashboard_stats(request):
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_customers = User.objects.count()
    data = {
        "total_products": total_products,
        "total_orders": total_orders,
        "total_customers": total_customers
    }
    return Response(data)

# ----- Log event API (no CSRF) -----
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def log_event(request):
    event = request.data.get('event')
    if event:
        print(f"Event received: {event}")
        return Response({"message": f"Event '{event}' logged successfully"})
    return Response({"error": "No event provided"}, status=400)
