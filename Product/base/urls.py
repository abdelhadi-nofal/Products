from django.urls import path
from . import views


urlpatterns=[
    path('',views.getRoutes,name='routes'),
    path('products/',views.getProducts,name='products'),
    path('products/<str:pk>/',views.getProduct,name='product'),
    path('product-create',views.addProduct,name='addproduct'),
    path('product-update/<str:pk>/',views.updateProduct,name='updateproduct'),
    path('product-delete/<str:pk>/',views.deleteProduct,name='deleteproduct'),
]