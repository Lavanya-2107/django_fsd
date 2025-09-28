from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from website.models import Product, Order
from website.serializers import ProductSerializer, OrderSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# ----- Product APIs -----
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all().values('id','name','description','price')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

# ----- Delete Product -----
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)

# ----- User Login -----
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
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
