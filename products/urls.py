from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('by_category/<int:pk>', views.ByCategory.as_view(), name='by-category'),
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('add_to_favorite', login_required(views.AddToFavorite.as_view())),
    path('favourite-products/', views.FavouriteProductsListView.as_view(), name='favourite-list'),
    path('', views.Index.as_view(), name='index-page'),
]
