from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'orders'


urlpatterns = [
    path('cart/', login_required(views.CartListView.as_view()), name='cart-list'),
    path('checkout/', login_required(views.CheckoutOrderView.as_view()), name='order-checkout'),
    path('update-cart/', views.update_cart, name='update-cart'),
    path('remove-order/<int:order_id>', views.remove_order, name='remove-order'),
    path('', login_required(views.OrdersListView.as_view()), name='orders-list'),
]
