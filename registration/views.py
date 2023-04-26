from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from registration.models import Subscription


class SignupView(AllauthSignupView):
    template_name = 'account/signup.html'


class LoginView(LoginView):
    template_name = 'account/login.html'


class LogoutView(LogoutView):
    template_name = 'account/logout.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class OurServiceView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = request.user.subscription
            if subscription.is_active:
                return render(request, 'our_service.html')
            else:
                return render(request, 'home.html', {'message': 'Please subscribe to access our service.'})
        except Subscription.DoesNotExist:
            return render(request, 'home.html', {'message': 'Please subscribe to access our service.'})
