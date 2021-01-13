from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'orders'


urlpatterns = [
    path('cart/', login_required(views.CartListView.as_view()), name='cart-list'),
    path('checkout/', login_required(views.CheckoutOrderView.as_view()), name='order-checkout'),
    path('', login_required(views.OrdersListView.as_view()), name='orders-list'),
]
