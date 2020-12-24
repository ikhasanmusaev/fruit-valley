from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('category/<slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('<slug>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('', views.ArticleListView.as_view(), name='blog-list'),
]
