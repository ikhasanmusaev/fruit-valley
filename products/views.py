from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View

from . import models
from .models import Product, Category


class Index(ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        return Product.objects.all()[0:10]


class ProductList(ListView):
    models = Product
    template_name = 'product_list.html'
    paginate_by = 10


class CategoryListView(ListView):
    models = Category
    paginate_by = 6
    template_name = 'category_list.html'

    def get_queryset(self):
        return Category.objects.all()[0:6]
