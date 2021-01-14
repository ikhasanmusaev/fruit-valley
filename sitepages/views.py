import datetime
import sys

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.views.decorators.csrf import csrf_exempt

from orders.models import Order
from products.models import Review


class SendMail(View):
    def post(self, request):
        if request.is_ajax():
            full_name = request.POST['full_name']
            email = request.POST['email']
            phone = request.POST['phone']
            content = request.POST['content']

            subject = 'Test message'
            from_email = settings.EMAIL_HOST_USER
            to_list = ['hm.musaev@yandex.com', ]

            message = ' Name: {} \n Email: {} \n Phone: {} \n Content: \n \n {}'.format(full_name,
                                                                                        email, phone, content)
            try:
                send_mail(subject, message, from_email, to_list)
            except Exception:
                e = sys.exc_info()
                print(e)
                return JsonResponse(status=403, data=({'error': ''}))
            else:
                return JsonResponse(status=200, data={'success': 'success'})
        else:
            return ''


class ContactUs(TemplateView):
    template_name = 'contact_us.html'


class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(status=True)[:6]
        return context


@csrf_exempt
def apelsin_payment(request):
    if request.method == "POST":
        # if request.user.id == 4:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        # {'orderId': '1', 'transaction_type': 'pay', 'amount': '50000', 'transactionId': '137458'}
        if ip == "87.237.235.235":
            data = request.data
            transaction_id = data['transactionId']
            amount = data['amount']
            order_id = data['orderId']
            transaction_type = ['transaction_type']
            date_now = datetime.datetime.now().timestamp()
            try:
                orders = Order.objects.get(id=int(order_id))
            except Order.MultipleObjectsReturned or Order.DoesNotExist:
                return JsonResponse(data={"status": False})
            else:
                if orders.status == 'waiting':
                    if orders.amount == amount[:-2]:
                        # orders.tran_id = transaction_id
                        # orders.method_pay = 'apelsin'
                        # orders.paid_date = int(date_now)
                        orders.status = 'paid'
                        orders.save()
                        return JsonResponse(data={"status": True})
                    else:
                        return JsonResponse(data={"status": False, "description": "Сумма оплаты не соответствует цене"})
                else:
                    return JsonResponse(data={"status": False}, status=403)
            # else:
            #     return JsonResponse(data={"status": False}, status=400)
        else:
            return JsonResponse(data={"status": False}, status=401)
    else:
        return JsonResponse(data={"status": False}, status=403)
