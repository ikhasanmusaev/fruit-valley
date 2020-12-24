from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.list import MultipleObjectMixin

from . import models
from .models import Category


class ArticleListView(ListView):
    model = models.Article
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.exclude(menu_position=0).order_by('menu_position')
        context['recent_posts'] = self.model.objects.filter(status=2).order_by('-id')
        return context

    def get_queryset(self):
        return self.model.objects.filter(status=2)


class CategoryDetailView(DetailView, MultipleObjectMixin):
    model = models.Category
    paginate_by = 5
    template_name = 'blogs/article_list.html'

    def get_context_data(self, **kwargs):
        object_list = models.Article.objects.filter(category=self.get_object())
        context = super(CategoryDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['category_list'] = Category.objects.exclude(menu_position=0).order_by('menu_position')
        context['recent_posts'] = models.Article.objects.filter(status=2).order_by('-id')
        context['article_list'] = models.Article.objects.filter(status=2, category__slug=self.kwargs['slug']).order_by('-id')
        return context


class ArticleDetailView(DetailView):
    models = models.Article
    template_name = 'blogs/article_detail.html'

    # slug_field = 'slug'

    def get_queryset(self):
        return self.models.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.exclude(menu_position=0).order_by('menu_position')
        context['recent_posts'] = models.Article.objects.filter(status=2).order_by('-id')
        return context
