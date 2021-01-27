from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView

from buyers import models as buyers
from products.models import Product, FavouriteProducts
from .models import Cart, PaymentMethods, Order


class CartListView(ListView):
    model = Cart
    template_name = 'orders/cart_list.html'

    def get_queryset(self):
        return self.model.objects.filter(buyer_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)
        context['total'] = round(self.model.total_of_cart(self.model, self.request.user.id))
        return context


    def post(self, request):
        if 'delete' in request.POST:
            self.model.objects.filter(id=request.POST['delete']).delete()
            return HttpResponse(status=202)

        if 'product_id' in request.POST:
            product = Product.objects.get(id=request.POST['product_id'])
            try:
                obj, created = Cart.objects.update_or_create(
                    buyer_id=request.user.id,
                    product_id=product.id,
                    defaults={
                        'type_of_selling': request.POST['type_of_selling']
                    }
                )

                if not created:
                    obj.total += int(request.POST['total'])
                    obj.amount = str(int(obj.amount) + int(request.POST['amount']))
                    obj.save()
                else:
                    obj.total = int(request.POST['total']) if int(request.POST['total']) else 1
                    obj.amount = request.POST['amount']
                    obj.save()

                return JsonResponse(data={}, status=200)
            except:
                return HttpResponse(status=403)

        return HttpResponse(status=403)


class CheckoutOrderView(ListView):
    model = Cart
    template_name = 'orders/checkout_order.html'

    def get_queryset(self):
        return self.model.objects.filter(buyer_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CheckoutOrderView, self).get_context_data(**kwargs)
        context['total'] = round(self.model.total_of_cart(self.model, self.request.user.id))
        context['payment_methods'] = PaymentMethods.objects.filter(status=True)
        context['buyer'] = buyers.Buyer.objects.filter(user_id=self.request.user.id)[0] if buyers.Buyer.objects.filter(user_id=self.request.user.id).exists() else None
        context['address'] = buyers.Address.objects.filter(user_id=self.request.user.id)[0] if buyers.Address.objects.filter(user_id=self.request.user.id).exists() else None
        return context

    def post(self, request):
        data = request.POST

        cart_ids = [data[x] for x in data if 'cart-' in x]

        carts = Cart.objects.filter(id__in=cart_ids)

        buyer, created_b = buyers.Buyer.objects.update_or_create(
            user_id=request.user.id,
            defaults={
                'full_name': data['name'],
                'company': data['company'] if 'company' in data else None,
                'phone': data['phone'],
                'add_email': data['email'] if 'email' in data else None,
                'add_info': data['add-info'] if 'add-info' in data else None,
            })
        address, created_a = buyers.Address.objects.update_or_create(
            user_id=request.user.id,
            defaults={
                'country': data['country'],
                'city': data['city'],
                'address_line1': data['address1'],
                'address_line2': data['address2'],
                'zip': data['zip_code'],
            },
        )
        order = Order.objects.create(
            buyer_id=buyer.id,
            price=data['total'],
            method_payment_id=data['method-payment'] if 'method-payment' in data else None,
        )
        products = []
        for i in carts:
            i.delete()
            products.append({
                'product_id': i.product.id,
                'name': i.product.name,
                'price': i.amount,
                'cart_id': i.id,
            })

        order.products = products
        order.save()

        return redirect('orders:orders-list')


class OrdersListView(ListView):
    model = Order
    template_name = 'orders/orders_list.html'

    def get_queryset(self):
        return Order.objects.filter(buyer_id=self.request.user.id)


@login_required
def remove_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'cancelled'
            order.save()
        except:
            return JsonResponse(data={}, status=301)
        return JsonResponse(data={}, status=200)
    return JsonResponse(data={}, status=301)
