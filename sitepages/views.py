import sys

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView

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
