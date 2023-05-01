from django.urls import path, include

from products.views import get_products_list

urlpatterns = [
    path("", get_products_list, name="products_list")
]
