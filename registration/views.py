import json
import math
import os

import requests
from allauth.account.views import LoginView, LogoutView
from allauth.account.views import SignupView as AllauthSignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from dotenv import find_dotenv, load_dotenv

from registration.models import Subscription

load_dotenv()
load_dotenv(find_dotenv(), override=True)

GEX_BOT_API_KEY = os.environ.get("GEX_BOT_API_KEY")
BASE_URL = "https://api.gexbot.com/spx"


class SignupView(AllauthSignupView):
    template_name = "account/signup.html"


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    template_name = "account/logout.html"


class HomePageView(TemplateView):
    template_name = "home.html"
            
class PathView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = Subscription.objects.get(user=request.user)
            if subscription.is_active:
                return render(request, "path.html")
            else:
                return render(
                    request,
                    "home.html",
                    {"message": "Please subscribe to access our service."},
                )
        except Subscription.DoesNotExist:
            return render(
                request,
                "home.html",
                {"message": "Please subscribe to access our service."},
            )
            
class HelpCalcView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = Subscription.objects.get(user=request.user)
            if subscription.is_active:
                return render(request, "help-calc.html")
            else:
                return render(
                    request,
                    "home.html",
                    {"message": "Please subscribe to access our service."},
                )
        except Subscription.DoesNotExist:
            return render(
                request,
                "home.html",
                {"message": "Please subscribe to access our service."},
            )


class MonthlySubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            plan_id = os.environ.get("LIVE_MONTHLY_PLAN_ID")
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            plan_id = os.environ.get("SANDBOX_MONTHLY_PLAN_ID")
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"plan_id": plan_id, "client_id": client_id}
        return render(request, "monthly_subscription.html", context=context)


class MonthlyStandardCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"client_id": client_id}
        return render(request, "monthly_standard_checkout.html", context=context)


class SemiAnnualStandardCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"client_id": client_id}
        return render(request, "semi_annual_standard_checkout.html", context=context)


class AnnualStandardCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"client_id": client_id}
        return render(request, "annual_standard_checkout.html", context=context)


class AnnualSubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            plan_id = os.environ.get("LIVE_ANNUAL_PLAN_ID")
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            plan_id = os.environ.get("SANDBOX_ANNUAL_PLAN_ID")
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"plan_id": plan_id, "client_id": client_id}
        return render(request, "annual_subscription.html", context=context)


class SemiAnnualSubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            plan_id = os.environ.get("LIVE_SEMI_ANNUAL_PLAN_ID")
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            plan_id = os.environ.get("SANDBOX_SEMI_ANNUAL_PLAN_ID")
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"plan_id": plan_id, "client_id": client_id}
        return render(request, "semi_annual_subscription.html", context=context)

@csrf_exempt
def create_subscription(request):
    print("create_subscription view called")
    if request.method == "POST":
        plan = request.POST.get("plan")
        order_id = request.POST.get("order_id")
        subscription_id = request.POST.get("subscription_id")
        payment_source = request.POST.get("payment_source")
        user = request.user
        print(f"DATA:{plan},{order_id},{subscription_id},{payment_source},{user}")

        subscription = Subscription.objects.create(
            user=user,
            plan=plan,
            order_id=order_id,
            subscription_id=subscription_id,
            payment_source=payment_source,
        )
        subscription.save()
        print("subscription added to the database")

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})


class GexBotAllFullView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/all/gex?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


@csrf_exempt
def save_subscription(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        user = request.user
        Subscription.objects.filter(user=user).delete()
        subscription = Subscription(
        user=user,
        payment_id=payload["payment_id"],
        currency_code=payload["currency_code"],
        amount_value=payload["amount_value"],
        full_name=payload["payer_fullname"],
        create_time=payload["create_time"],
        end_date=payload["end_date"],  # Set the end_date based on your requirements
        is_active=True,  # Set the is_active field to True for new subscriptions
        )

        subscription.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


class GexBotZeroFullView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/zero/gex?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


class GexBotAllMajorsView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/all/majors?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


class GexBotZeroMajorsView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/zero/majors?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


class GexBotAllMaxView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/all/maxchange?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


class GexBotZeroMaxView(LoginRequiredMixin, View):
    def get(self, request):
        url = f"{BASE_URL}/zero/maxchange?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


class SpxView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = Subscription.objects.get(user=request.user)
            if subscription.is_active:
                context = {"api_key": GEX_BOT_API_KEY}
                return render(request, "spx.html", context)
            else:
                return render(
                    request, "home.html", {"message": "Please subscribe to access SPX."}
                )
        except Subscription.DoesNotExist:
            return render(
                request, "home.html", {"message": "Please subscribe to access SPX."}
            )

class ErrorPageView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'error_page.html')