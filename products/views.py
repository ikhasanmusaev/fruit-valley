from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models

# class ProductListView(DetailView):


def index(request):
    print(1)
    return render(request, 'index.html')
