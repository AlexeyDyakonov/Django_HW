from django.urls import path
from django.views.generic import DetailView

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name = 'product_list'),
    path('products/<int:pk>/', CatalogDetailView.as_view(), name = 'product_detail'),
    path('products/create', CatalogCreateView.as_view(), name = 'product_create'),
    path('products/<int:pk>/update/', CatalogUpdateView.as_view(), name = 'product_update'),
    path('products/<int:pk>/delete/', CatalogDeleteView.as_view(), name = 'product_delete'),
]