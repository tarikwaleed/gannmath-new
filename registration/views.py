from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.urls import reverse_lazy


class SignupView(AllauthSignupView):
    template_name = 'account/signup.html'


class LoginView(LoginView):
    template_name = 'account/login.html'


class LogoutView(LogoutView):
    template_name = 'account/logout.html'
