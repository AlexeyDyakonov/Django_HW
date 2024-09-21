from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, about_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name = 'product_list'),
    path('products/<int:pk>/', about_product, name = 'about_product'),
]