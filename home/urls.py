from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('products/', ProductsAPI.as_view()),
    path('products/<int:id>/', ProductDetailsAPI.as_view()),
    path('product_details/<int:id>/', product_details),
]