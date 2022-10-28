from django.shortcuts import render
from rest_framework import generics as api_generic_views, permissions
from rest_framework import views as api_views
from rest_framework import serializers
# This should be in file 'serializers.py'
from rest_framework.response import Response

from django_rest_framework_demos.api_demos.models import Product, Category


class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ManualProductsListView(api_views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


'''
    ListAPIView
    RetrieveAPIView
    CreateAPIView
    DestroyAPIView
    UpdateAPIView
'''


class ProductsListView(api_generic_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    # def get_queryset(self):


class CategoriesListView(api_generic_views.ListCreateAPIView):
    queryset = Category.objects.all()
    # serializer_class = FullCategorySerializer


class SingleProductView(api_generic_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
