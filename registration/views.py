import datetime
from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from registration.models import Subscription
import os
from dotenv import load_dotenv,find_dotenv
from django.views.decorators.csrf import csrf_exempt
load_dotenv()
load_dotenv(find_dotenv(), override=True)


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


class MonthlySubscriptionView(LoginRequiredMixin, View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_MONTHLY_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "monthly_subscription.html",context=context)

class AnnualSubscriptionView(LoginRequiredMixin,View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_ANNUAL_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "annual_subscription.html",context=context)
class SemiAnnualSubscriptionView(LoginRequiredMixin,View):
    def get(self, requst):
        plan_id=os.environ.get('SANDBOX_SEMI_ANNUAL_PLAN_ID')
        client_id=os.environ.get('SANDBOX_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "semi_annual_subscription.html",context=context)


@csrf_exempt
def create_subscription(request):
    print('create_subscription view called')
    if request.method == 'POST':
        plan = request.POST.get('plan')
        order_id = request.POST.get('order_id')
        subscription_id = request.POST.get('subscription_id')
        payment_source = request.POST.get('payment_source')
        user = request.user
        print(f'DATA:{plan},{order_id},{subscription_id},{payment_source},{user}')
        
        
        subscription = Subscription.objects.create(
            user=user,
            plan=plan,
            order_id=order_id,
            subscription_id=subscription_id,
            payment_source=payment_source
        )
        subscription.save()
        print("subscription added to the database")
        
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
