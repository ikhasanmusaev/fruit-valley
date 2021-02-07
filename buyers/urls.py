from django.contrib.auth.decorators import login_required

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include, reverse_lazy

app_name = 'buyers'

urlpatterns = [
    path('password/change/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('buyers:password_change_done'),
        template_name='accounts/password_change_form.html',
    ),
         name='password_change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html',
    ), name='password_change_done'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ),
         name='password_reset_complete'),
    re_path(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset_confirm.html',
                success_url=reverse_lazy('buyers:password_reset_complete')
            ),
            name='password_reset_confirm'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url=reverse_lazy('buyers:password_reset_done'),
        template_name='accounts/password_reset_form.html',
    ), name='password_reset'),
    # path('authentication/', views.Signup.as_view(), name='login_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('signup/', views.SignupView.as_view(), name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('', views.AccountView.as_view(), name='account'),
    path('details/', login_required(views.AccountDetailsView.as_view()), name='account-details'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('activate/<str:uid>/<str:token>', views.Activate.as_view(), name='activate'),
]
