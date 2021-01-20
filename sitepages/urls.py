from django.urls import path, re_path

from . import views

app_name = 'site_pages'

urlpatterns = [
    path('send_email', views.SendMail.as_view(), name='send_mail'),
    path('contacts/', views.ContactUs.as_view(), name='contacts'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('apelsin/payment/', views.apelsin_payment),
    re_path('search/', views.SearchView.as_view(), name='search'),
]
