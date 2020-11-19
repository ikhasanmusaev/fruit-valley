from . import views
from django.urls import path

app_name = 'buyers'

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('activate/<str:uid>/<str:token>', views.Activate.as_view(), name='activate'),
]
