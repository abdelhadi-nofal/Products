from django import views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(req):
    return Response(
        {
        'Products':'api/products',
        'Product Detail':'api/products/<str:pk>',
        'Create':'api/product-create',
        'Update':'api/product-update/<str:pk>',
        'Delete':'api/product-delete/<str:pk>',
        })

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request,pk):
    product= Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many= False)

    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request,pk):
    product= Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProduct(request,pk):
    product= Product.objects.get(id=pk)
    product.delete()
    return Response('Product Deleted Succesfully')


    



