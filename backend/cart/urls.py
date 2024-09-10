from django.urls import path
from . import views


urlpatterns = [
    path('add', views.add_product_cart, name='add_product_cart'),
    path('', views.product_cart_list, name='product_cart_list'),
]
