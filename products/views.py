from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, DeleteView
import json

from blogs.models import Article
from orders.models import Cart
from sitepages.models import SlideOfProduct
from .models import Product, Category, Review, FavouriteProducts


class Index(ListView):
    model = Product
    template_name = '_home_page/home.html'

    def get_queryset(self):
        return Product.objects.all()[0:10]

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['slide_of_product_list'] = SlideOfProduct.objects.all()[0:6]
        context['articles'] = Article.objects.all()[0:4]
        context['categories'] = Category.objects.filter(status=True, product__isnull=False)[0:6]
        context['reviews'] = Review.objects.filter(status=True)[:6]
        context['favourites'] = [i.product_id for i in FavouriteProducts.objects.filter(user_id=1)]
        return context


class CategoryListView(ListView):
    models = Category
    paginate_by = 8
    template_name = 'categories/category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['parents'] = Category.active_categories(True)
        return context

    def get_queryset(self):
        return Category.active_categories()


class CategoryDetailView(DetailView):
    models = Category
    template_name = 'categories/category_list.html'

    def get_queryset(self):
        return Category.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category_list'] = self.models.active_categories()
        context['parents'] = Category.active_categories(True)
        context['product_list'] = Product.objects.filter(category__slug=self.kwargs['slug'])
        context['is_item'] = True
        return context


class ByCategory(View):
    def post(self, request):
        return render(request, '_home_page/home.html')

    def get(self, request, pk):
        if request.is_ajax():
            if pk != 0:
                products = Product.objects.filter(category_id=pk)[0:9]
            else:
                products = Product.objects.all()[0:9]
            products_list = []
            data = {}
            for i in products:
                data['id'] = i.id
                data['name'] = i.name
                data['price'] = i.price_for_qty
                data['rating_stars'] = i.rating_stars
                data['image'] = i.image.file.url
                data['sale'] = i.get_sale()
                products_list.append(data)
                data = {}
            return JsonResponse({'data': products_list})
        else:
            return ''


class ProductDetailView(DetailView):
    model = Product
    template_name = '_product_page/product_detail.html'

    def get_queryset(self):
        product = Product.objects.get(id=self.kwargs['pk'])
        return Product.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product_id=self.kwargs['pk'], status=True)
        context['favorite'] = FavouriteProducts.objects.filter(product_id=self.kwargs['pk'], user_id=1).exists()
        context['similar_products'] = Product.objects.filter(category_id=kwargs['object'].category_id)[0:4]
        return context


class AddToFavorite(View):
    def post(self, request):
        if request.is_ajax():
            product_id = request.POST['product_id']
            product = Product.objects.get(id=int(product_id))

            obj, created = FavouriteProducts.objects.update_or_create(
                product_id=product_id,
                user_id=1
            )
            if not created:
                obj.delete()

            return JsonResponse({'created': created}, status=201)
        else:
            return ''

    def get(self, request):
        return render(request, '_home_page/home.html')


class FavouriteProductsListView(ListView):
    model = FavouriteProducts
    template_name = 'wishlist.html'

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)

