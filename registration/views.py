from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from registration.models import Subscription
import os
from dotenv import load_dotenv
load_dotenv()


class SignupView(AllauthSignupView):
    template_name = "account/signup.html"


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    template_name = "account/logout.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class OurServiceView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = request.user.subscription
            if subscription.is_active:
                return render(request, "our_service.html")
            else:
                return render(request, "home.html", {"message": "Please subscribe to access our service."})
        except Subscription.DoesNotExist:
            return render(request, "home.html", {"message": "Please subscribe to access our service."})


class MonthlySubscriptionView(View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_MONTHLY_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "monthly_subscription.html",context=context)

class AnnualSubscriptionView(View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_ANNUAL_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "annual_subscription.html",context=context)
class SemiAnnualSubscriptionView(View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_SEMI_ANNUAL_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "semi_annual_subscription.html",context=context)