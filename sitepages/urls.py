from django.urls import path, re_path

from . import views

app_name = 'site_pages'

urlpatterns = [
    path('send_email', views.SendMail.as_view(), name='send_mail'),
    path('contacts/', views.ContactUs.as_view(), name='contacts'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('apelsin/payment/', views.apelsin_payment),
    re_path('search/', views.SearchView.as_view(), name='search'),
    re_path('stripe_config/', views.stripe_config, name='stripe-config'),
    re_path('create-checkout-session/', views.create_checkout_session, name='stripe-config'),
    re_path('success-stripe/', views.success_stripe, name='stripe-success'),
    re_path('subscribe/', views.create_subscribe, name='subscribe'),
]
