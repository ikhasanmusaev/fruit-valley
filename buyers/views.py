from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View, generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from django.contrib.auth import views as auth_views

from .forms import SignupForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import User, Buyer, Address
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import login, update_session_auth_hash, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm


def logout_view(request):
    logout(request)
    return redirect('products:index-page')


# class Signup(View):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.signup_form = SignupForm()
#         self.login_form = LoginForm()
#
#     def get(self, request):
#         return render(request, 'accounts/login.html', {'sign_form': self.signup_form, 'login_form': self.login_form})
#
#     def post(self, request):
#         if 'signup_' in request.POST:
#             form = SignupForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.is_active = False
#                 user.save()
#                 current_site = get_current_site(request)
#                 mail_subject = 'Activate your blog account.'
#                 message = render_to_string('acc_active_email.html', {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 })
#                 to_email = form.cleaned_data.get('email')
#                 email = EmailMessage(
#                     mail_subject, message, to=[to_email]
#                 )
#                 email.send()
#                 return render(request, '_partials/message.html',
#                               {'message', 'Please confirm your email address to complete the registration'})
#         if 'signin_' in request.POST:
#             form = LoginForm(data=request.POST)
#             if form.is_valid():
#                 user = form.get_user()
#                 login(request, user, backend='buyers.backends.EmailBackend')
#                 if 'next' in request.POST:
#                     return redirect(request.POST.get('next'))
#                 else:
#                     return redirect('products:index-page')
#             else:
#                 messages.error(request, 'username or password not correct')
#                 return render(request, 'accounts/login.html', {'sign_form': self.signup_form, 'login_form': self.login_form})
#         return render(request, 'accounts/login.html', {'sign_form': self.signup_form, 'login_form': self.login_form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='buyers.backends.EmailBackend')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:index-page')
        return render(request, 'accounts/login.html', {'form': form})


class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        logout(request)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'

            message = render_to_string('acc_active_email.html',
                                       context={
                                           'user': user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': account_activation_token.make_token(user),
                                       },
                                       request=request)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            message_text = 'Please confirm your email address to complete the registration'
            return render(request, '_partials/message.html', {'message_text': message_text})
        return render(request, 'accounts/signup.html', {'form': form})


class Activate(View):
    def get(self, request, uid, token, backend='buyers.backends.EmailBackend'):
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            # activate user and login:
            user.is_active = True
            user.save()
            login(request, user, backend='buyers.backends.EmailBackend')

            form = PasswordChangeForm(request.user)
            # return render(request, '_home_page/home.html')
            return render(request, 'activation.html', {'form': form, 'uid': uid, 'token': token})

        else:
            return HttpResponse('Activation link is invalid!')

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('products:index-page')


class AccountView(TemplateView):
    template_name = 'accounts/account.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['buyer'] = Buyer.objects.filter(user_id=self.request.user.id)[0] if Buyer.objects.filter(
            user_id=self.request.user.id).exists() else None
        context['address'] = Address.objects.filter(user_id=self.request.user.id)[0] if Address.objects.filter(
            user_id=self.request.user.id).exists() else None
        return context

    def post(self, request):
        data = request.POST
        buyer, created_b = Buyer.objects.update_or_create(
            user_id=request.user.id,
            defaults={
                'full_name': data['name'],
                'company': data['company'] if 'company' in data else None,
                'phone': data['phone'],
                'add_email': data['email'] if 'email' in data else None,
                'add_info': data['add-info'] if 'add-info' in data else None,
            })
        address, created_a = Address.objects.update_or_create(
            user_id=request.user.id,
            defaults={
                'country': data['country'],
                'city': data['city'],
                'address_line1': data['address1'],
                'address_line2': data['address2'],
                'zip': data['zip_code'],
            },
        )

        return redirect('products:index-page')


class AccountDetailsView(TemplateView):
    template_name = 'accounts/account-details.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailsView, self).get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(self.request.user)
        return context

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('products:index-page')
        return redirect('products:index-page')
