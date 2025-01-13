from rest_framework.views import APIView
from rest_framework.response import Response
from .product_recommender import get_similar_products
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import render
# Create your views here.

def index(request):
  return render(request, 'index.html')

def product_details(request, id):
  context = {id: id}
  return render(request, 'product_details.html', context)

class ProductsAPI(APIView):
  def get(self, request):
    products = Product.objects.all().order_by("?")[:40]
    serializer = ProductSerializer(products, many=True)
    return Response({
      "all_products": serializer.data
    })

class ProductDetailsAPI(APIView):
  def get(self, request, id):
    products = Product.objects.get(id=id)
    serializer = ProductSerializer(products)
    similar_products = get_similar_products(id, top_n=10)
    similar_products_serializer = ProductSerializer(similar_products, many=True)
    return Response({
      "product": serializer.data,
      "similar_products": similar_products_serializer.data
    })