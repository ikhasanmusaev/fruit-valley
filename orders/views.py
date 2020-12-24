from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from products.models import Product, FavouriteProducts
from .models import Cart, PaymentMethods


class CartListView(ListView):
    model = Cart
    template_name = 'orders/cart_list.html'

    def get_queryset(self):
        return self.model.objects.filter(buyer_id=self.request.user.id)

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

                return HttpResponse(status=201)
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
        context['total'] = self.model.total_of_cart(self.model, self.request.user.id)
        context['payment_methods'] = PaymentMethods.objects.filter(status=True)
        return context

    def post(self, request):
        return
