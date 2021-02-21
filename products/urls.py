from django.contrib import admin
from django.urls import path, include
from .views import ListProduct, DetailsProduct, ListCategory, DetailsCategory, ListSize, DetailsSize


urlpatterns = [
    path("products/", ListProduct.as_view(), name="Productos"),
    path("products/<int:pk>/", DetailsProduct.as_view(), name="Producto"),
    path("category/", ListCategory.as_view(), name="Categorias"),
    path("category/<int:pk>/", DetailsCategory.as_view(), name="Categoria"),
    path("size/", ListSize.as_view(), name="Tamaños"),
    path("size/<int:pk>/", DetailsSize.as_view(), name="Tamaño"),
]
