from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('<int:order_id>', views.order_detail, name='order_detail'),
]
