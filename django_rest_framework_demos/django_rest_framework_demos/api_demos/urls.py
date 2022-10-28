from django.urls import path

from django_rest_framework_demos.api_demos.views import ManualProductsListView, ProductsListView, SingleProductView

urlpatterns = [
    path('products-manual/', ManualProductsListView.as_view(), name='products manual list'),
    path('products/', ProductsListView.as_view(), name='products list'),
    path('products/<int:pk>/', SingleProductView.as_view(), name='single product'),
]
