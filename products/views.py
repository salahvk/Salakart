from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductModelSerializer
# Create your views here.

def index(request) :
    return render(request,'index.html')

def list_products(request) :
    product_list = Product.objects.all() 
    context = {'products':product_list}
    return render(request, 'products.html',context)

def detail_product(request) :
    return render(request, 'product_detail.html')

class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Product.objects.all()
 
    # specify serializer to be used
    serializer_class = ProductModelSerializer

